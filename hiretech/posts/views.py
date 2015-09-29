from django.shortcuts import render

from django.views.generic import ListView,DetailView
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

class PostIndex(ListView):
    template_name = 'post_index.html'
    def get(self,request):
        post_list = Post.objects.filter(status='published').order_by('-published_date')
        paginator = Paginator(post_list, 20)
        page = request.GET.get('page')

        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)

        context = {
            'post_list': post_list,
        }
        return render(
            request,
            self.template_name,
            context
        )
