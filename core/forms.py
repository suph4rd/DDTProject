from django import forms
from core import models
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )


class UserAdminForm(forms.ModelForm):
    password = forms.PasswordInput()

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        if user.password != self.cleaned_data["password"]:
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = models.User
        fields = ['username', 'password', 'first_name', 'last_name', 'patronymic', 'position',
                  'is_staff', 'is_superuser']


class StaffModelForm(forms.Form):
    type = forms.ChoiceField(
        choices=models.STAFF_CHOICES,
        label='Тип'
    )
    name = forms.ModelChoiceField(
        queryset=models.Staff.objects.none(),
        required=False,
        label='Название'
    )


class UnionInteresModelForm(forms.Form):
    type = forms.ChoiceField(
        choices=models.UNION_INTERES_CHOICES_TYPE,
        label='Тип'
    )
    profile = forms.ModelChoiceField(
        queryset=models.UnionInteresProfile.objects.none(),
        required=False,
        label='Профиль'
    )
