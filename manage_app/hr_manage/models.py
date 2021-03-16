from django.db import models
from common.baseModel import BaseModel


# Create your models here.
class OAClient(BaseModel):
    name = models.CharField(verbose_name="名字", max_length=20)
    file_type = models.CharField(verbose_name="文件类型", max_length=20)
    file_name = models.CharField(verbose_name="文件名", max_length=100)
    file_path = models.CharField(verbose_name="路径", max_length=200)

    class Meta:
        db_table = "oa_client"
        verbose_name = "客户管理"


class OADepartment(BaseModel):
    dep_name = models.CharField(verbose_name="部门", max_length=20)
    position = models.CharField(verbose_name="职位", max_length=20)

    class Meta:
        db_table = "oa_department"
        verbose_name = "部门管理"


class OAStaff(BaseModel):
    name = models.CharField(verbose_name="名字", max_length=20)
    gender = models.CharField(verbose_name="性别", max_length=20)
    age = models.IntegerField(verbose_name="年龄")
    department_id = models.IntegerField(verbose_name="部门id")

    class Meta:
        db_table = "oa_staff"
        verbose_name = "员工管理"
