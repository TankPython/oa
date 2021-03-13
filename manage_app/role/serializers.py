from .models import OARole, OAUser, OAPermission
from rest_framework import serializers


class OaRoleSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)

    def get_children(self, obj):
        return obj.get_role_ps()

    class Meta:
        model = OARole
        fields = ['id', 'name', 'desc', 'ps_ids', 'children']
        extra_kwargs = {'ps_ids': {'write_only': True}}


class OaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OAUser
        fields = ['id', 'name', 'email', 'password', 'phone', 'role_id']
        extra_kwargs = {'password': {'write_only': True}}


class OaPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OAPermission
        fields = ['id', 'name', 'method', 'pid', 'level', 'path']
        extra_kwargs = {'pid': {'write_only': True}}
