from .models import OARole, OAUser, OAPermission
from rest_framework import serializers
from common.utils import create_md5


class OaRoleSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)

    def get_children(self, obj):
        if not obj.ps_ids:
            return []
        role_ids = [pid for pid in obj.ps_ids.split(",")]
        permissions = OAPermission.objects.filter(deleted=False, id__in=role_ids)
        result_list = []

        # 第一级权限
        ps_obj_level_0_list = permissions.filter(level=0, pid=0)
        for ps_obj_level_0 in ps_obj_level_0_list:
            data_level_0 = {
                "id": ps_obj_level_0.id,
                "authName": ps_obj_level_0.name,
                "path": ps_obj_level_0.path,
                "children": []
            }

            # 第二级权限
            ps_obj_level_1_list = permissions.filter(level=1, pid=ps_obj_level_0.id)
            for ps_obj_level_1 in ps_obj_level_1_list:
                data_level_1 = {
                    "id": ps_obj_level_1.id,
                    "authName": ps_obj_level_1.name,
                    "path": ps_obj_level_1.path,
                    "children": []
                }
                data_level_0["children"].append(data_level_1)
            result_list.append(data_level_0)
        return result_list

    class Meta:
        model = OARole
        fields = ['id', 'name', 'desc', 'ps_ids', 'children']
        extra_kwargs = {'ps_ids': {'write_only': True}}


class OaUserSerializer(serializers.ModelSerializer):
    # role = serializers.SerializerMethodField(read_only=True)
    #
    # def get_role(self, obj):
    #     role = OARole.objects.filter(id=obj.role_id).first()
    #     if role:
    #         return role.name
    #     else:
    #         return ""

    class Meta:
        model = OAUser
        fields = ['id', 'name', 'email', 'password', 'phone', 'role_id']
        extra_kwargs = {'password': {'write_only': True}}


class OaPermissionSerializer(serializers.ModelSerializer):
    # parent_ps = serializers.SerializerMethodField()

    # def get_parent_ps(self, obj):
    #     parent_ps = OAPermission.objects.filter(id=obj.role_id).first()
    #     if parent_ps:
    #         return parent_ps.name
    #     else:
    #         return ""

    class Meta:
        model = OAPermission
        fields = ['id', 'name', 'method', 'pid', 'level', 'path']
        extra_kwargs = {'pid': {'write_only': True}}
