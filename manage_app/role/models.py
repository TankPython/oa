from django.db import models
from django.utils import timezone
from common.baseModel import BaseModel


# Create your models here.
class OAUser(BaseModel):
    name = models.CharField(verbose_name="名字", max_length=20)
    password = models.CharField(verbose_name="密码", max_length=20)
    email = models.CharField(verbose_name="邮箱", max_length=100, blank=True)
    phone = models.CharField(verbose_name="电话", blank=True, max_length=15)
    role_id = models.IntegerField(verbose_name="角色id", blank=True, null=True)

    class Meta:
        db_table = "oa_user"
        verbose_name = "用户表"


class OARole(BaseModel):
    name = models.CharField(verbose_name="名字", max_length=20, blank=True)
    desc = models.CharField(verbose_name="描述", max_length=20, blank=True)
    ps_ids = models.CharField(verbose_name="拥有的权限id", max_length=300, blank=True)

    class Meta:
        db_table = "oa_role"
        verbose_name = "角色表"


class OAPermission(BaseModel):
    name = models.CharField(verbose_name="名字", max_length=20)
    method = models.CharField(verbose_name="请求方法", max_length=20)
    pid = models.IntegerField(verbose_name="上级id")
    level = models.IntegerField(verbose_name="等级")
    path = models.CharField(verbose_name="请求路径", max_length=200)

    class Meta:
        db_table = "oa_permission"
        verbose_name = "权限表"
