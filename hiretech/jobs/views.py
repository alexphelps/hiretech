from django.http import Http404
from django.template import RequestContext, loader
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants as MSG
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError,PermissionDenied
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseRedirect,
)
from django.shortcuts import get_object_or_404,render
from django.views.generic import TemplateView,View,ListView
from taggit.models import Tag
from .forms import JobAddForm
from .models import Job
from companies.models import Company
from users.models import UserProfile
from search.forms import CustomSearchForm
from hiretech.decorators import userincompany

# Create your views here.
class JobIndex(ListView):
    template_name = 'job_index.html'
    def get(self,request):
        form = CustomSearchForm(request.GET, searchqueryset=None)
        jobs_list = Job.objects.filter(job_status='published').order_by('-job_created_date')
        paginator = Paginator(jobs_list, 30)
        page = request.GET.get('page')

        try:
            jobs_list = paginator.page(page)
        except PageNotAnInteger:
            jobs_list = paginator.page(1)
        except EmptyPage:
            jobs_list = paginator.page(paginator.num_pages)

        context = {
            'form': form,
            'jobs_list': jobs_list,
        }
        return render(
            request,
            self.template_name,
            context
        )

class JobAddNew(TemplateView):
    template_name = 'job_add.html'
    @userincompany
    def get(self,request,company_slug, **kwargs):
        company = kwargs['company']
        form = JobAddForm()
        context = {
            'current_user_companies':kwargs['current_user_companies'],
            'form':form,
            'company':kwargs['company'],
        }
        return render(
            request,
            self.template_name,
            context
        )
    @userincompany
    def post(self,request,company_slug, **kwargs):
        company = kwargs['company']
        form = JobAddForm(request.POST)
        if form.is_valid():
            job_author = request.user
            job_company = get_object_or_404(Company, company_slug=company_slug)
            job_title = form.cleaned_data['job_title']
            job_location = form.cleaned_data['job_location']
            tags = form.cleaned_data['tags']
            job_type = form.cleaned_data['job_type']
            job_description = form.cleaned_data['job_description']
            job_responsibilities = form.cleaned_data['job_responsibilities']
            job_qualifications = form.cleaned_data['job_qualifications']
            job_notes = form.cleaned_data['job_notes']
            job_apply_method = form.cleaned_data['job_apply_method']
            job_apply_link = form.cleaned_data['job_apply_link']
            job = Job.objects.create(
                job_author=job_author,
                job_company=job_company,
                job_title=job_title,
                job_location=job_location,
                job_type=job_type,
                job_description=job_description,
                job_responsibilities=job_responsibilities,
                job_qualifications=job_qualifications,
                job_notes=job_notes,
                job_status='published',
                job_apply_method=job_apply_method,
                job_apply_link=job_apply_link,
            )
            for each in tags:
                lowertag = each.lower()
                job.tags.add(lowertag)

            success_msg = 'Woohoo! Your job posting has been published.'
            messages.add_message(
                self.request,
                MSG.SUCCESS,
                success_msg
            )
            return HttpResponseRedirect(
                reverse('dashboard')
            )

        else:
            error_msg = 'Please see required fields below.'
            messages.add_message(
                self.request,
                MSG.ERROR,
                error_msg
            )

        context = {
            'current_user_companies':kwargs['current_user_companies'],
            'form':form,
            'company':kwargs['company'],
        }
        return render(
            request,
            self.template_name,
            context
        )


class JobDetails(TemplateView):
    template_name = 'job_details.html'
    def get(self,request,**kwargs):
        job_id = self.kwargs['job_id']
        job = get_object_or_404(Job, pk=job_id)
        tags = job.tags.all()
        context = {
            'job': job,
            'tags': tags,
        }
        return render(
            request,
            self.template_name,
            context
        )

class JobMarkAsFilled(View):
    def get(self, request,**kwargs):
        job_id = self.kwargs['job_id']
        job = get_object_or_404(Job, pk=job_id)
        jobcompany = job.job_company
        current_user = request.user
        current_user_id = current_user.id
        current_user_profile = UserProfile.objects.get(user__id=current_user_id)
        current_user_account = current_user_profile.account.id
        current_user_account_companies = Company.objects.filter(account=current_user_account)
        if jobcompany in current_user_account_companies:
            job.job_status='filled'
            job.save()
            success_msg = 'Great Job! Your job was filled.'
            messages.add_message(
                self.request,
                MSG.SUCCESS,
                success_msg
            )
            return HttpResponseRedirect(
                reverse('dashboard')
            )
        else:
            raise PermissionDenied
