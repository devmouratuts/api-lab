from rest_framework import viewsets
from labapp.api import serializers
from labapp import models
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from labapp.permissions import NoDeletePermission


class LabAppViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LabAppSerializer
    queryset = models.LabApp.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,NoDeletePermission,)
    


  


    











