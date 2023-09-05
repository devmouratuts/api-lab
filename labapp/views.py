from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import LabApp
from django.shortcuts import render



def inativar_usuario(request, user_id):
    usuario = LabApp.objects.get(id_usuario=user_id)

    if request.method == 'POST':
        usuario.is_active = False  # Defina o status de ativação como False para inativar o usuário
        usuario.save()
        messages.success(request, 'Usuário inativado com sucesso.')
        return redirect('lista_de_usuarios')  # Redirecione para a página de lista de usuários ou outra página apropriada

    return render(request, 'inativar_usuario.html', {'usuario': usuario})





