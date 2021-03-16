from .models import OAStaff, OADepartment, OAClient
from rest_framework import serializers


class OAClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OAClient
        fields = ['id', 'name', 'file_type', 'file_name', 'file_path']


class OADepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OADepartment
        fields = ['id', 'name', 'position']


class OAStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = OAStaff
        fields = ['id', 'name', 'gender', 'age', 'department_id']
