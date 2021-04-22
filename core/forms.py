from django import forms
from core import models
from django.contrib.auth.forms import AuthenticationForm


class StaffModelForm(forms.Form):
    type = forms.ChoiceField(
        choices=models.STAFF_CHOICES,
        label='Тип'
    )
    name = forms.ModelChoiceField(
        queryset=models.Staff.objects.all(),
        required=False,
        label='Название'
    )


class CustomAuthenticationForm(AuthenticationForm):
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
