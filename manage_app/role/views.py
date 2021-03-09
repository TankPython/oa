from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from rest_framework import permissions
from .models import OARole
from .serializers import OaRoleSerializer
from common.utils import CusPagination


class RoleViewSet(APIView):

    def get(self, request):
        oaRoles = OARole.objects.filter()
        serialize = OaRoleSerializer(oaRoles, many=True)
        page = CusPagination()
        return page.get_paginated_response(["dfdf0","fdfdf"])
