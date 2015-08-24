from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf import settings
# Create your views here.
from .models import Company
from jobs.models import Job

def company_details(request, company_id):
    #get all open jobs
    company = get_object_or_404(Company, pk=company_id)
    company_job_list = Job.objects.filter(job_company=company)
    template = loader.get_template('company_details.html')
    context = RequestContext(request, {
        'company_job_list': company_job_list,
        'company': company,
    })
    return HttpResponse(template.render(context))
