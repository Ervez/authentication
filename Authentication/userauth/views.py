from django.shortcuts import render


def HomePage(request):
    return render(request, 'templates/home.html')


def SignupPage(request):
    pass


def LoginPage(request):
    pass


def home(request):
    return render(request, 'userauth/home.html')
