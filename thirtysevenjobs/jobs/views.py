from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Job
# Create your views here.
def index(request):
    #get all questions
    jobs_list = Job.objects.order_by('-job_created_date')
    template = loader.get_template('jobs/index.html')
    context = RequestContext(request, {
        'jobs_list': jobs_list,
    })
    return HttpResponse(template.render(context))

def jobdetail(request, job_id):
    return HttpResponse("You're looking at job %s." % job_id)
