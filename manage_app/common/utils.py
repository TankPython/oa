from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response
from rest_framework import authentication
from rest_framework import exceptions, HTTP_HEADER_ENCODING
from rest_framework.permissions import BasePermission
from django.core.cache import cache
from .result_code import rest_code
from copy import deepcopy
import hashlib
import uuid


def create_token():
    return str(uuid.uuid1())


def create_md5(str):
    return hashlib.md5(str.encode()).hexdigest()


def get_result(data="success"):
    rest = deepcopy(rest_code.get(data))
    return rest


class CusPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pagesize'
    page_query_param = 'pagenum'
    max_page_size = 100

    def get_single(self, request, model, ser):
        json_data = request.GET.dict()
        id = json_data.get("id")
        obj = model.objects.filter(deleted=False, id=id).first()
        return ser(obj).data

    def get_list(self, request, model, ser, query_field="name"):
        if request.GET.get("query", ""):
            query_parms = request.GET.get("query")
            object_list = model.objects.filter(deleted=False).filter(
                **{"{}__contains".format(query_field): query_parms})

        else:
            object_list = model.objects.filter(deleted=False)
        return ser(object_list, many=True).data

    def cus_query(self, request, model, ser):
        json_data = request.GET.dict()
        id = json_data.get("id")
        if id:
            data = self.get_single(request, model, ser)
            return self.single_result(data)
        else:
            data = self.get_list(request, model, ser)
            self.paginate_queryset(data, request)
            return self.get_paginated_response(self.page.object_list)

    # 返回单条数据
    def single_result(self, data):
        rest = get_result()
        rest.update({"data": data})
        return Response(rest)

    # 返回带页面的多条数据
    def get_paginated_response(self, data):
        rest = get_result()
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
        path = request.path
        method = request.method
        if path == "/api/menu/":
            return True
        from role.models import OAPermission, OARole
        role_id = request.user.role_id
        if not role_id:
            return False
        role = OARole.objects.filter(id=role_id).first()
        ps_ids = role.ps_ids
        if not ps_ids:
            return False
        ps_ids = ps_ids.split(",")
        ps = OAPermission.objects.filter(path=path, method=method.lower()).first()
        if str(ps.id) not in ps_ids:
            return False
        return True


print(create_md5("123456"))
