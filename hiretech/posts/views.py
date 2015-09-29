from django.shortcuts import render

from django.views.generic import TemplateView,DetailView
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from .models import Post,Category
# Create your views here.
class PostSingle(DetailView):
    template_name = 'post_single.html'
    def get(self,request,slug):
        post = get_object_or_404(Post,slug=slug)
        context = {
            'post': post,
        }
        return render(
            request,
            self.template_name,
            context
        )
