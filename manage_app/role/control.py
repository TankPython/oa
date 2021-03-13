from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from rest_framework import permissions
from .models import OARole, OAUser, OAPermission
from .serializers import OaRoleSerializer, OaUserSerializer
from common.utils import CusPagination, get_result, create_token
from django.core.cache import cache
import traceback


class RoleControl:
    def __init__(self, json_data):
        self.json_data = json_data

    def delete_target_ps_to_role(self):
        resp = get_result()
        try:
            json_data = self.json_data
            role_id = json_data.get("id")
            ps_id = str(json_data.get("ps_id"))
            role = OARole.objects.filter(deleted=False, id=role_id).first()
            ps_ids = role.ps_ids.split(",")
            if ps_id in ps_ids:
                ps_ids.remove(ps_id)
            ps_ids = ",".join(ps_ids)

            # save to database
            data = {
                "ps_ids": ps_ids,
            }
            serialize = OaRoleSerializer(role, data=data, partial=True)
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

    def put_role(self):
        resp = get_result()
        try:
            json_data = self.json_data
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
