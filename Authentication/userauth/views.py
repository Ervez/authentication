from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
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
    return render(request, 'userauth/login.html')
