from .models import OARole
from rest_framework import serializers


class OaRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OARole
        fields = ['name', 'desc', 'ps_ids']
