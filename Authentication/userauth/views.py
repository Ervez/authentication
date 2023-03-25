from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .forms import RegisterUserForm


def HomePage(request):
    return render(request, 'userauth/home.html')


def SignupPage(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Pomyślnie zarejestrowano")
            return redirect(HomePage)
    else:
        form = RegisterUserForm()

    return render(request, 'userauth/register.html', {'form': form})


def LoginPage(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(HomePage)
        else:
            return redirect(LoginPage)

    return render(request, 'userauth/login.html')


def UserLogout(request):
    logout(request)
    return redirect(HomePage)
