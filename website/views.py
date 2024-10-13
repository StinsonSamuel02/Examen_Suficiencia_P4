from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.

@login_required
def home(request):
    return render(request, 'pages/home.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username is None or password is None:
            error = "Introduzca usuario y contraseña válidos"
            return render(request, 'pages/signin.html', {'error': error})
        user = authenticate(username=username, password=password)
        if user is None:
            error = "Credenciales Inválidas"
            return render(request, 'pages/signin.html', {'error': error})

        login(request, user)
        return redirect('/')
    return render(request, 'pages/signin.html')


def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')
