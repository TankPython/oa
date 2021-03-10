from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response
from rest_framework import authentication
from rest_framework import exceptions, HTTP_HEADER_ENCODING
from rest_framework.permissions import BasePermission
from django.core.cache import cache
from .result_code import rest_code
from copy import deepcopy


def get_result(data):
    rest = deepcopy(rest_code.get(data))
    return rest


class CusPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pagesize'
    page_query_param = 'pagenum'
    max_page_size = 100

    def cus_query(self, request, model, ser):
        if request.GET.get("query", ""):
            query_parms = request.GET.get("query")
            object_list = model.objects.filter(name__contains=query_parms)

        else:
            object_list = model.objects.all()
        return ser(object_list, many=True).data


    def get_paginated_response(self, data):
        rest = get_result("success")
        rest.update({"data": {
            'pagenum': self.page.number,
            'totalpage': self.page.paginator.count,
            'results': data
        }})
        return Response(rest)


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
