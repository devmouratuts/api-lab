from rest_framework import serializers
from labapp import models



class Meta:
        permissions = [
            ("no_delete_LabApp", "Can't delete LabApp"),
        ]

class LabAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LabApp
        fields = '__all__'