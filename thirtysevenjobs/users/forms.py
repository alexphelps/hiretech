from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User

from companies.models import Company

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
        )
    company_logo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'id': 'company_logo',
                'class': 'form-control'
            }),
        required=False)