from django.db import models
from uuid import uuid4

# Create your models here.

class LabApp(models.Model):
    id_usuario = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=200, unique=True)
    user_type_id = models.SmallIntegerField(max_length=2)
    password = models.CharField(max_length=100)
    is_active = models.SmallIntegerField(max_length=2)
    cpf_cnpj = models.CharField(max_length=14, unique=True)
    phone = models.IntegerField(max_length=14)
