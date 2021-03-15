from django.db import models
from django.utils import timezone
from common.baseModel import BaseModel


# Create your models here.
class OAUser(BaseModel):
    name = models.CharField(verbose_name="名字", max_length=20)
    password = models.CharField(verbose_name="密码", max_length=32)
    email = models.CharField(verbose_name="邮箱", max_length=100, blank=True)
    phone = models.CharField(verbose_name="电话", max_length=15, blank=True)
    role_id = models.IntegerField(verbose_name="角色id", blank=True, null=True)

    def validate_pwd(self, password):
        from common.utils import create_md5
        return create_md5(password) == self.password

    def create_password(self):
        from common.utils import create_md5
        return create_md5(self.password)

    class Meta:
        db_table = "oa_user"
        verbose_name = "用户表"


class OARole(BaseModel):
    name = models.CharField(verbose_name="名字", max_length=20)
    desc = models.CharField(verbose_name="描述", max_length=20, blank=True, null=True)
    ps_ids = models.CharField(verbose_name="拥有的权限id", max_length=300, blank=True, null=True)

    def get_role_ps(self):
        ps_ids = self.ps_ids
        if not ps_ids:
            return []
        ps_ids = ps_ids.split(",")
        ps_ids = [int(i) for i in ps_ids]
        base_query = OAPermission.objects.filter(deleted=False).filter(id__in=ps_ids)
        return OAPermission.get_permission(base_query)

    class Meta:
        db_table = "oa_role"
        verbose_name = "角色表"


class OAPermission(BaseModel):
    name = models.CharField(verbose_name="名字", max_length=20)
    method = models.CharField(verbose_name="请求方法", max_length=20)
    pid = models.IntegerField(verbose_name="上级id")
    level = models.IntegerField(verbose_name="等级")
    path = models.CharField(verbose_name="请求路径", max_length=200)

    @staticmethod
    def get_permission(base_query):
        rest_list = []
        base_ps_list = base_query.filter(pid=0, level=0)
        for base_ps in base_ps_list:
            rest_data = {}
            rest_data["id"] = base_ps.id
            rest_data["authName"] = base_ps.name
            rest_data["path"] = base_ps.path
            rest_data["pid"] = base_ps.pid
            rest_data["children"] = []

            ps_level2_list = base_query.filter(pid=base_ps.id)
            for ps_level2 in ps_level2_list:
                rest_data2 = {
                    "id": ps_level2.id,
                    "authName": ps_level2.name,
                    "path": ps_level2.path,
                    "pid": ps_level2.pid,
                    "children": []
                }

                ps_level3_list = base_query.filter(pid=ps_level2.id)
                for ps_level3 in ps_level3_list:
                    rest_data2["children"].append({
                        "id": ps_level3.id,
                        "authName": ps_level3.name,
                        "path": ps_level3.path,
                        "pid": ps_level3.pid,
                    })

                rest_data["children"].append(rest_data2)
            rest_list.append(rest_data)
        return rest_list

    class Meta:
        db_table = "oa_permission"
        verbose_name = "权限表"
