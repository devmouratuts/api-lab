from django.db import models
from uuid import uuid4



# Create your models here.

class LabApp(models.Model):
    id_usuario = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=200, unique=True)
    
    USER_TYPE_CHOICES = (
        (0, 'Admin'),
        (1, 'Usuario'),
    )

    user_type_id = models.SmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    password = models.CharField(max_length=100)

    IS_ACTIVE_CHOICES = (
        (0, 'Ativo'),
        (1, 'Inativo'),
    )

    is_active = models.SmallIntegerField(choices=IS_ACTIVE_CHOICES, default=1)
    cpf_cnpj = models.CharField(max_length=14, unique=True)
    phone = models.IntegerField()

    


    def set_user_type_id(self, value):
        if value == 0:
            # Se o user_type_id for 0, definir o usuário como administrador
            self.user_type_id = 0
            
        else:
            # Se o user_type_id não for 0, definir como não-administrador (1)
            self.user_type_id = 1

    def set_is_active(self, value):
        if value == 0:
            # Se o is_active for 0, definir o usuário como ativo
            self.is_active = 0

        else:
            # Se o is_active não for 0, definir como inativo (1)
            self.is_active = 1            


    








    