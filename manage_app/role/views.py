from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from rest_framework import permissions
from .models import OARole, OAUser, OAPermission
from .serializers import OaRoleSerializer, OaUserSerializer
from common.utils import CusPagination, get_result, create_token, create_md5
from django.core.cache import cache
import traceback
from .control import RoleControl


class Login(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        resp = get_result()
        try:
            json_data = request.data
            password = json_data.get("password")
            name = json_data.get("name")
            user = OAUser.objects.filter(deleted=False, name=name).first()
            # 用户不存在或者密码错误
            if not user or not user.validate_pwd(password):
                return JsonResponse(get_result("PasswordOrUsernameError"))
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(get_result("ParamsError"))

        # 请求成功
        token = create_token()
        cache.set(token, user.id, 6000)
        oaUserSer = OaUserSerializer(user)
        user_data = oaUserSer.data
        user_data.update({"token": token})
        resp.update({"data": user_data})
        return JsonResponse(resp)


class Register(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        resp = get_result()
        try:
            json_data = request.data
            name = json_data.get("name")
            stu = OAUser.objects.filter(name=name, deleted=False).first()
            # 用户已经存在
            if stu:
                return JsonResponse(get_result("UserExits"))
            if json_data.get("password", ""):
                json_data["password"] = create_md5(json_data["password"])
            serialize = OaUserSerializer(data=json_data)
            if serialize.is_valid():
                serialize.save()
            else:
                return JsonResponse(get_result("ParamsError"))
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(get_result("ParamsError"))

        # 请求成功
        return JsonResponse(resp)


class RoleView(APIView):

    def get(self, request):
        page = CusPagination()
        return page.cus_query(request, OARole, OaRoleSerializer)

    # 增加role
    def post(self, request):
        resp = get_result()
        try:
            json_data = request.data
            serialize = OaRoleSerializer(data=json_data)
            if serialize.is_valid():
                serialize.save()
            else:
                return JsonResponse(get_result("ParamsError"))
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(get_result("ParamsError"))

        # 请求成功
        return JsonResponse(resp)

    def delete(self, request):
        resp = get_result()
        try:
            json_data = request.GET.dict()
            id = json_data.get("id")
            role = OARole.objects.filter(deleted=False, id=id).first()
            if role.name == "admin":
                return JsonResponse(get_result("NoAuthOperateSuperuser"))
            # role = OARole.objects.filter(deleted=False, id=id)
            role.delete()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(get_result("ParamsError"))

        # 请求成功
        return JsonResponse(resp)

    # 修改role
    def put(self, request):
        json_data = request.data
        id = json_data.get("id")
        role = OARole.objects.filter(deleted=False, id=id).first()
        if role.name == "admin":
            return JsonResponse(get_result("NoAuthOperateSuperuser"))
        action = json_data.get("act")
        roleControl = RoleControl(json_data)
        if action == "delete_target_ps_to_role":
            return roleControl.delete_target_ps_to_role()
        else:
            return roleControl.put_role()


class UserView(APIView):

    def get(self, request):
        json_data = request.GET
        if json_data.get("act") == "self":
            resp = get_result()
            resp.update({"data": OaUserSerializer(request.user).data})
            return JsonResponse(resp)
        else:
            page = CusPagination()
            return page.cus_query(request, OAUser, OaUserSerializer)

    # 增加user
    def post(self, request):
        resp = get_result()
        try:
            json_data = request.data
            name = json_data.get("name")
            user = OAUser.objects.filter(name=name, deleted=False).first()
            # 用户已经存在
            if user:
                return JsonResponse(get_result("UserExits"))
            if json_data.get("password", ""):
                json_data["password"] = create_md5(json_data["password"])
            serialize = OaUserSerializer(data=json_data, partial=True)
            if serialize.is_valid():
                serialize.save()
            else:
                return JsonResponse(get_result("ParamsError"))
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(get_result("ParamsError"))

        # 请求成功
        resp.update({"data": serialize.data})
        return JsonResponse(resp)

    def delete(self, request):
        resp = get_result()
        try:
            json_data = request.GET.dict()
            id = json_data.get("id")
            user = OAUser.objects.filter(deleted=False, id=id).first()
            if user.name == "admin":
                return JsonResponse(get_result("NoAuthOperateSuperuser"))
            user.delete()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(get_result("ParamsError"))

        # 请求成功
        return JsonResponse(resp)

    def put(self, request):
        resp = get_result()
        try:
            json_data = request.data
            id = json_data.get("id")
            user = OAUser.objects.filter(deleted=False, id=id).first()
            if user.name == "admin":
                return JsonResponse(get_result("NoAuthOperateSuperuser"))
            if json_data.get("password", ""):
                json_data["password"] = create_md5(json_data["password"])
            serialize = OaUserSerializer(instance=user, data=json_data, partial=True)
            if serialize.is_valid():
                serialize.save()
            else:
                print(serialize.errors)
                return JsonResponse(get_result("ParamsError"))
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(get_result("ParamsError"))

        # 请求成功
        return JsonResponse(resp)


class MenuView(APIView):
    # 获取自己拥有的菜单、权限
    def get(self, request):
        resp = get_result()
        user = request.user
        rest_list = []
        if not user.role_id:
            resp.update({"data": rest_list})
            return JsonResponse(resp)
        role = OARole.objects.filter(deleted=False, id=user.role_id).first()
        ps_ids = role.ps_ids
        if not ps_ids:
            resp.update({"data": rest_list})
            return JsonResponse(resp)

        resp.update({"data": role.get_role_ps()})
        return JsonResponse(resp)


class RightView(APIView):
    # 获取所有权限
    def get(self, request):
        resp = get_result()
        rest = OAPermission.get_permission(OAPermission.objects.filter(deleted=False))
        resp.update({"data": rest})
        return JsonResponse(resp)
