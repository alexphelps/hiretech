from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf import settings
from search.forms import CustomSearchForm
from jobs.models import Job

class HomepageView(TemplateView):
    template_name = 'index.html'
    def get(self,request):
        form = CustomSearchForm(request.GET, searchqueryset=None)
        user = request.user
        recent_five_jobs_list = Job.objects.filter(job_status='published').order_by('-job_created_date')[:5]
        context = {
            'user':user,
            'form': form,
            'recent_five_jobs_list':recent_five_jobs_list,
        }
        return render(
            request,
            self.template_name,
            context
        )
