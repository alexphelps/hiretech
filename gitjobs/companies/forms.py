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

    def save(self, company):
        company.company_name = self.cleaned_data['company_name']
        company.company_url = self.cleaned_data['company_url']
        company.save()
