from .models import OARole, OAUser, OAPermission
from rest_framework import serializers


class OaRoleSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    def get_permissions(self, obj):
        if not obj.ps_ids:
            return []
        role_ids = [pid for pid in obj.ps_ids.split(",")]
        permissions = OAPermission.objects.filter(id__in=role_ids)
        if permissions:
            return [p.name for p in permissions]
        else:
            return []

    class Meta:
        model = OARole
        fields = ['id', 'name', 'desc', 'permissions']


class OaUserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField(read_only=True)

    def get_role(self, obj):
        role = OARole.objects.filter(id=obj.role_id).first()
        if role:
            return role.name
        else:
            return ""


    class Meta:
        model = OAUser
        fields = ['id', 'name', 'email', 'phone', 'role']


class OaPermissionSerializer(serializers.ModelSerializer):
    parent_ps = serializers.SerializerMethodField()

    def get_parent_ps(self, obj):
        parent_ps = OAPermission.objects.filter(id=obj.role_id).first()
        if parent_ps:
            return parent_ps.name
        else:
            return ""

    class Meta:
        model = OAPermission
        fields = ['id', 'name', 'method', 'parent_ps', 'level', 'path']
