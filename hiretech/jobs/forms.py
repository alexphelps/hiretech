from django import forms
from taggit.forms import *
from companies.models import Company

class JobAddForm(forms.Form):
    job_title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'job_title',
                'class': 'form-control'
            }),
        required=True)
    job_location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'job_location',
                'class': 'form-control'
            }),
        required=True)
    tags = TagField(
        widget=TagWidget(
            attrs={
                'id': 'tags',
                'class': 'form-control tokenfield'
            }),
        )
    job_type = forms.ChoiceField(
        choices=(
            ('full_time','Full Time'),
            ('part_time','Part Time'),
            ('contract','Contract'),
            ('internship','Internship')
        ),
        widget=forms.Select(
            attrs={
            'id': 'job_type',
            'class': 'form-control'
            }),
        required=True)
    job_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'id': 'job_description',
                'class': 'form-control',
                'rows':'6'
            }),
        required=True)
    job_responsibilities = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'id': 'job_responsibilities',
                'class': 'form-control',
                'rows':'6'
            }),
        required=True)
    job_qualifications = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'id': 'job_qualifications',
                'class': 'form-control',
                'rows':'6'
            }),
        required=True)
    job_notes = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'id': 'job_notes',
                'class': 'form-control',
                'rows':'4'
            }),
        required=False)
    job_apply_method = forms.ChoiceField(
        choices=(
            ('link','Link'),
            ('email','Email'),
        ),
        widget=forms.Select(
            attrs={
            'id': 'job_apply_method',
            'class': 'form-control apply-select'
            }),
        required=True)
    job_apply_link = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'job_apply_link',
                'class': 'form-control',
            }),
        required=True)
