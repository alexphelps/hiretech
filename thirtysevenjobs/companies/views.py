from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf import settings
# Create your views here.
from .models import Company
from jobs.models import Job

class CompanyDetails(TemplateView):
    template_name = 'company_details.html'
    def get(self,request, **kwargs):
        company_id = self.kwargs['company_id']
        company = get_object_or_404(Company, pk=company_id)
        company_job_list = Job.objects.filter(job_company=company)
        context = {
            'company_job_list': company_job_list,
            'company': company,
        }
        return render(
            request,
            self.template_name,
            context
        )

class CompanyEditView(TemplateView):
    template_name = 'company_edit.html'
    def get(self,request, **kwargs):
        company_id = self.kwargs['company_id']
        company = get_object_or_404(Company, pk=company_id)
        context = {

        }
        return render(
            request,
            self.template_name,
            context
        )
