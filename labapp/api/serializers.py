from rest_framework import serializers
from labapp import models

class LabAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LabApp
        fields = '__all__'