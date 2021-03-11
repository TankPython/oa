from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from rest_framework import permissions
from .models import OARole, OAUser
from .serializers import OaRoleSerializer, OaUserSerializer
from common.utils import CusPagination, get_result, create_token
from django.core.cache import cache
import traceback


class Login(APIView):
    authentication_classes = []

    def post(self, request):
        resp = get_result()
        try:
            json_data = request.POST.dict()
            password = json_data.get("password")
            name = json_data.get("name")
            stu = OAUser.objects.filter(name=name).first()
            # 用户不存在或者密码错误
            if not stu or not stu.validate_pwd(password):
                return JsonResponse(get_result("PasswordOrUsernameError"))
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(get_result("ParamsError"))

        # 请求成功
        token = create_token()
        cache.set(token, stu.id, 6000)
        resp.update({"token": token})
        return JsonResponse(resp)


class Register(APIView):
    authentication_classes = []

    def post(self, request):
        resp = get_result()
        try:
            json_data = request.POST.dict()
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
            json_data = request.POST.dict()
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
            json_data = request.POST.dict()
            id = json_data.get("id")
            role = OARole.objects.filter(deleted=False, id=id).first()
            serialize = OaRoleSerializer(role, data=json_data)
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
        return page.cus_query(request, OARole, OaRoleSerializer)

    # 增加user
    def post(self, request):
        resp = get_result()
        try:
            json_data = request.POST.dict()
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
            json_data = request.POST.dict()
            id = json_data.get("id")
            user = OAUser.objects.filter(deleted=False, id=id).first()
            serialize = OaUserSerializer(user, data=json_data)
            if serialize.is_valid():
                serialize.save()
            else:
                return JsonResponse(get_result("ParamsError"))
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(get_result("ParamsError"))

        # 请求成功
        return JsonResponse(resp)
