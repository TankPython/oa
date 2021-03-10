from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from rest_framework import permissions
from .models import OARole, OAUser
from .serializers import OaRoleSerializer
from common.utils import CusPagination
import uuid
from django.core.cache import cache


class Login(APIView):
    authentication_classes = []

    def get(self, request):
        stu = OAUser.objects.get(name=request.GET.get("name"))
        if stu:
            token = str(uuid.uuid1())
            cache.set(token, stu.id, 6000)
            return JsonResponse({"token": token})


class RoleViewSet(APIView):
    authentication_classes = []

    def get(self, request):
        page = CusPagination()
        query = page.cus_query(request, OARole, OaRoleSerializer)
        page.paginate_queryset(query, request)
        return page.get_paginated_response(page.page.object_list)
