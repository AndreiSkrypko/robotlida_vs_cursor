from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Пароль",
        min_length=3,
        help_text="Минимум 3 символа"
    )

    class Meta:
        model = User
        fields = ('username',)
        labels = {
            'username': 'Имя пользователя'
        }
        help_texts = {
            'username': ''  # Убираем стандартную подсказку Django
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")