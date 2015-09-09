from django import forms
from .models import Company

class CompanyEditForm(forms.Form):
    company_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'company_name',
                'class': 'form-control'
            }),
        required=True)

    company_url = forms.URLField(
        widget=forms.TextInput(
            attrs={
                'id': 'company_url',
                'class': 'form-control'
            }),
        required=True)
