from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=20, label="Nazwa użytkownika")
    password1 = forms.CharField(
        label="Hasło",
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Potwierdź hasło",
        strip=False,
        widget=forms.PasswordInput,
    )
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50, label="Imię")
    last_name = forms.CharField(max_length=50, label="Nazwisko")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
