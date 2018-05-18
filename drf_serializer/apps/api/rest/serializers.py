from rest_framework import serializers
from apps.timelines.models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id','text', 'user']