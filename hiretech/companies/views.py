from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import constants as MSG
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError,PermissionDenied
from django.views.generic import TemplateView,DetailView,UpdateView
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
# Create your views here.
from .forms import CompanyEditForm
from .models import Company
from jobs.models import Job
from users.models import UserProfile
from hiretech.decorators import userincompany

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
    @userincompany
    def get(self,request, company_slug, **kwargs):
        company = kwargs['company']
        initial = {
            'company_name': company.company_name,
            'company_url' : company.company_url,
        }
        form = self.form(initial=initial)
        context = {
            'form':form,
            'company': kwargs['company'],
        }
        return render(
            request,
            self.template_name,
            context
        )
    @userincompany
    def post(self,request,company_slug, **kwargs):
        form = CompanyEditForm(request.POST,request.FILES)
        company = kwargs['company']
        company_logo = ''
        company_featured_image = ''
        if form.is_valid():
            if 'company_logo' in request.FILES:
                company_logo = request.FILES['company_logo']
            if 'company_featured_image'in request.FILES:
                company_featured_image = request.FILES['company_featured_image']
            form.save(company,request,company_logo,company_featured_image)
            success_msg = 'Company Details Updated.'
            messages.add_message(
                request,
                MSG.SUCCESS,
                success_msg
            )
            return HttpResponseRedirect(
                reverse('dashboard'),
            )
        else:
            error_msg = 'Please see required fields below.'
            messages.add_message(
                request,
                MSG.ERROR,
                error_msg
            )
            context = {
                'form':form,
                'company': kwargs['company'],
            }
            return render(
                request,


                self.template_name,
                context
            )
