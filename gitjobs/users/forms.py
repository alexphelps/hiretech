
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.contrib.messages import constants as MSG

from nocaptcha_recaptcha.fields import NoReCaptchaField
from companies.models import Company
from .models import UserProfile

class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'id': 'email',
                'class': 'form-control'
            }),
        required=True)

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'class':'form-control'
            }),
        required=True)

class PasswordResetRequestForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'id': 'email',
                'class': 'form-control'
            }),
        required=True)

class PasswordResetNewPassword(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'new_password',
                'class':'form-control'
            }),
        required=True)

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'new_password2',
                'class':'form-control'
            }),
        required=True)

class SignupForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'first_name',
                'class': 'form-control'
            }),
        required=True)

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'last_name',
                'class': 'form-control'
            }),
        required=True)

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'id': 'email',
                'class': 'form-control'
            }),
        required=True)

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'class':'form-control'
            }),
        required=True)

    company_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'company_name',
                'class': 'form-control'
            }),
        )
    company_url = forms.CharField(
        widget=forms.URLInput(
            attrs={
                'id': 'company_url',
                'class': 'form-control'
            }),
        required=False)
    company_logo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'id': 'company_logo',
                'class': 'form-control'
            }),
        required=True)

    captcha = NoReCaptchaField()

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        email = cleaned_data.get("email")
        users_count = User.objects.filter(username=email).count()
        if users_count > 0:
            raise forms.ValidationError(
                    _('The email already is already in use.',
                    params={'value': '42'
                    })
                )
        return self.cleaned_data

class UserEditForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'first_name',
                'class': 'form-control'
            }),
        required=True)

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'last_name',
                'class': 'form-control'
            }),
        required=True)

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'id': 'email',
                'class': 'form-control'
            }),
        required=True)

    def save(self,user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
class PasswordUpdateForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'new_password',
                'class':'form-control'
            }),
        required=True)
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'new_password',
                'class':'form-control'
            }),
        required=True)

    new_password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'new_password',
                'class':'form-control'
            }),
        required=True)
