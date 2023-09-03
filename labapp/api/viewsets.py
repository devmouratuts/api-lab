from rest_framework import viewsets
from labapp.api import serializers
from labapp import models

class LabAppViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LabAppSerializer
    queryset = models.LabApp.objects.all()