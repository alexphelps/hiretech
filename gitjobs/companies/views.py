from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf import settings
# Create your views here.
from .forms import CompanyEditForm
from .models import Company
from jobs.models import Job

class CompanyDetails(DetailView):
    template_name = 'company_details.html'
    def get(self,request, company_slug):
        company = get_object_or_404(Company, company_slug=company_slug)
        company_active_job_list = Job.objects.filter(job_company=company,job_status='published')
        context = {
            'company_active_job_list': company_active_job_list,
            'company': company,
        }
        return render(
            request,
            self.template_name,
            context
        )

class CompanyEditView(TemplateView):
    template_name = 'company_edit.html'
    form = CompanyEditForm

    def get(self,request, company_slug):
        company = get_object_or_404(Company, company_slug=company_slug)
        initial = {
            'company_name': company.company_name,
            'company_url' : company.company_url,
        }
        form = self.form(initial=initial)
        context = {
            'form':form,
        }
        return render(
            request,
            self.template_name,
            context
        )
