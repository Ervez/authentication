from django.shortcuts import render


def HomePage(request):
    return render(request, 'userauth/home.html')


def SignupPage(request):
    pass


def LoginPage(request):
    return render(request, 'userauth/home.html')

