from django import forms
from django.template import RequestContext, loader
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
    company_logo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'id': 'company_logo',
                'class': 'form-control'
            }),
        required=False)

    def save(self, company,request,compnay_logo):
        company.company_name = self.cleaned_data['company_name']
        company.company_url = self.cleaned_data['company_url']
        if request.FILES:
            company.company_logo = request.FILES['company_logo']
        company.save()
