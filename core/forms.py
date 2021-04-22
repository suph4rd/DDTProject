from django import forms
from core import models
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )


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


class UnionInteresModelForm(forms.Form):
    type = forms.ChoiceField(
        choices=models.UNION_INTERES_CHOICES_TYPE,
        label='Тип'
    )
    profile = forms.ModelChoiceField(
        queryset=models.UnionInteresProfile.objects.all(),
        required=False,
        label='Профиль'
    )
