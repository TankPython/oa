from django.db import models
from django.utils import timezone
from common.baseModel import BaseModel


# Create your models here.
class OAUser(BaseModel):
    name = models.CharField(verbose_name="名字", max_length=20, unique=True)
    password = models.CharField(verbose_name="密码", max_length=32)
    email = models.CharField(verbose_name="邮箱", max_length=100, blank=True)
    phone = models.CharField(verbose_name="电话", max_length=15, blank=True)
    role_id = models.IntegerField(verbose_name="角色id", blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.password:
            self.password = self.create_password()
        return super(OAUser, self).save(*args, **kwargs)

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
