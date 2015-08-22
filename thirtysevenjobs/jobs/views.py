from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Job
# Create your views here.
def index(request):
    #get all questions
    jobs_list = Job.objects.all().order_by('-job_created_date')
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'jobs_list': jobs_list,
    })
    return HttpResponse(template.render(context))

def jobdetail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'job_details.html', {'job': job})
