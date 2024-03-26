from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib import auth, messages

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
    return render(request,'users/index.html',context)

def logout(request):
    auth.logout(request)
    return redirect('users:login')