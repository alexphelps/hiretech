from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf import settings

def homepage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
