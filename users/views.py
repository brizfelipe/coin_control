from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Perfil
from django.conf import settings

# Create your views here.
def login(request):
    context = {}
    context['form'] = LoginForm
    if request.method == 'POST':
        access = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=access).exists():
            name = User.objects.filter(username=access).get().username
            user = auth.authenticate(request, username=name, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home:index')
            else:
                messages.error(request, 'Cuidado, Parece que seu usuário ou senha está inválido, verifique e tente novamente.')
        else:
            messages.error(request, 'Ops! Parece que você ainda não está cadastrado')
    return render(request,'users/login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('users:login')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('users:login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def perfil(request):
    context = {}
    # Obtenha o perfil do usuário logado
    perfil_usuario = Perfil.objects.get(user=request.user)
    context['perfil'] = perfil_usuario
    # Adicione a URL da imagem de perfil ao contexto
    context['foto_perfil'] = perfil_usuario.foto_perfil.url
    return render(request, 'users/perfil.html', context)

