from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants as MSG
from django.views.generic import TemplateView,ListView,DetailView
from taggit.models import Tag
from .forms import JobAddForm
from .models import Job
from companies.models import Company
from users.models import UserProfile

# Create your views here.
class JobIndex(TemplateView):
    template_name = 'job_index.html'
    def get(self,request):
        jobs_list = Job.objects.all().order_by('-job_created_date')
        context = {
            'jobs_list': jobs_list,
        }
        return render(
            request,
            self.template_name,
            context
        )

class JobAddNew(TemplateView):
    template_name = 'job_add.html'
    def get(self,request):
        form = JobAddForm()
        current_user = request.user
        current_user_id = current_user.id
        current_user_profile = UserProfile.objects.get(user__id=current_user_id)
        context = {
            'current_user_profile':current_user_profile,
            'form':form,
        }
        return render(
            request,
            self.template_name,
            context
        )
    def post(self,request):
        form = JobAddForm(request.POST)
        current_user = request.user
        current_user_id = current_user.id
        current_user_profile = UserProfile.objects.get(user__id=current_user_id)
        current_user_company = current_user_profile.company
        if form.is_valid():
            job_company = current_user_company
            job_title = form.cleaned_data['job_title']
            job_location = form.cleaned_data['job_location']
            tags = form.cleaned_data['tags']
            job_type = form.cleaned_data['job_type']
            job_description = form.cleaned_data['job_description']
            job_responsibilities = form.cleaned_data['job_responsibilities']
            job_qualifications = form.cleaned_data['job_qualifications']
            job_notes = form.cleaned_data['job_notes']
            job = Job.objects.create(
                job_company=job_company,
                job_title=job_title,
                job_location=job_location,
                job_type=job_type,
                job_description=job_description,
                job_responsibilities=job_responsibilities,
                job_qualifications=job_qualifications,
                job_notes=job_notes,
                job_status='published',
            )
            for each in tags:
                lowertag = each.lower()
                job.tags.add(lowertag)

        else:
            print form.errors
            error_msg = 'Please see required fields below.'
            messages.add_message(
                self.request,
                MSG.ERROR,
                error_msg
            )

        context = {
            'current_user_profile': current_user_profile,
            'form':form,
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
