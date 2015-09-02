from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf import settings
from django.views.generic import TemplateView

from .models import Job
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

class JobDetails(TemplateView):
    template_name = 'job_details.html'
    def get(self,request,**kwargs):
        job_id = self.kwargs['job_id']
        job = get_object_or_404(Job, pk=job_id)
        context = {
            'job': job
        }
        return render(
            request,
            self.template_name,
            context
        )
