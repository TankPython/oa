from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from rest_framework import permissions
from .models import OARole, OAUser, OAPermission
from .serializers import OaRoleSerializer, OaUserSerializer
from common.utils import CusPagination, get_result, create_token
from django.core.cache import cache
import traceback


class Login(APIView):
    authentication_classes = []

    def post(self, request):
        resp = get_result()
        try:
            json_data = request.data
            password = json_data.get("password")
            name = json_data.get("name")
            user = OAUser.objects.filter(name=name).first()
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

    def post(self, request):
        resp = get_result()
        try:
            json_data = request.data
            name = json_data.get("name")
            stu = OAUser.objects.filter(name=name).first()
            # 用户已经存在
            if stu:
                return JsonResponse(get_result("UserExits"))
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
    authentication_classes = []

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
            role = OARole.objects.filter(deleted=False, id=id)
            role.delete()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(get_result("ParamsError"))

        # 请求成功
        return JsonResponse(resp)

    # 修改role
    def put(self, request):
        resp = get_result()
        try:
            json_data = request.data
            id = json_data.get("id")
            role = OARole.objects.filter(deleted=False, id=id).first()
            serialize = OaRoleSerializer(role, data=json_data, partial=True)
            if serialize.is_valid():
                serialize.save()
            else:
                return JsonResponse(get_result("ParamsError"))
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(get_result("ParamsError"))

        # 请求成功
        return JsonResponse(resp)


class UserView(APIView):
    authentication_classes = []

    def get(self, request):
        page = CusPagination()
        return page.cus_query(request, OAUser, OaUserSerializer)

    # 增加user
    def post(self, request):
        resp = get_result()
        try:
            json_data = request.data
            serialize = OaUserSerializer(data=json_data)
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
            role = OAUser.objects.filter(deleted=False, id=id)
            role.delete()
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
    authentication_classes = []

    def get(self, request):
        resp = get_result()
        base_ps_list = OAPermission.objects.filter(deleted=False, pid=0, level=0)
        rest_list = []
        for base_ps in base_ps_list:
            rest_data = {}
            rest_data["id"] = base_ps.id
            rest_data["authName"] = base_ps.name
            rest_data["path"] = base_ps.path
            rest_data["pid"] = base_ps.pid
            rest_data["children"] = []
            ps_level2_list = OAPermission.objects.filter(deleted=False, pid=base_ps.id)
            for ps_level2 in ps_level2_list:
                rest_data["children"].append({
                    "id": ps_level2.id,
                    "authName": ps_level2.name,
                    "path": ps_level2.path,
                    "pid": ps_level2.pid,
                })
            rest_list.append(rest_data)
        resp.update({"data": rest_list})
        return JsonResponse(resp)
