from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response
from rest_framework import authentication
from rest_framework import exceptions, HTTP_HEADER_ENCODING
from rest_framework.permissions import BasePermission
from django.core.cache import cache


class CusPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.

    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, str):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


class CusAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        from role.models import OAUser
        token = get_authorization_header(request)
        uid = cache.get(token.decode())
        try:
            user = OAUser.objects.get(id=uid)
        except Exception as e:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, token)

    def authenticate_header(self, request):
        print("authenticate header")
        return "token"


class CusPermission(BasePermission):
    def has_permission(self, request, view):
        print("has permission")
        print(request.user.id)
        return True
