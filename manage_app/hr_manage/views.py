from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from rest_framework import permissions
from .models import OAClient, OADepartment, OAStaff
from .serializers import OAClientSerializer, OAStaffSerializer, OADepartmentSerializer
from common.utils import CusPagination, get_result, create_token, create_md5,upload_file
from django.core.cache import cache
import traceback


class Client(APIView):
    def get(self, request):
        page = CusPagination()
        return page.cus_query(request, OAClient, OAClientSerializer)

    # 增加
    def post(self, request):
        filte_obj = request.files.get("file")
        json_data = request.data
        upload_file(file_obj=filte_obj)




class Department(APIView):
    pass


class Staff(APIView):
    pass


class Sign(APIView):
    pass
