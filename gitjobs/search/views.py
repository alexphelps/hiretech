from django.shortcuts import render

from django.views.generic import TemplateView

from .forms import CustomSearchForm
from jobs.models import Job

class CustomSearchView(TemplateView):
    template_name = 'search/search.html'

    def get(self, request):
        query = ''
        results = ''
        form = CustomSearchForm(request.GET, searchqueryset=None)
        if form.is_valid():
            query = form.cleaned_data['q']
            results = form.search()
        context = {
            'form': form,
            'query': query,
            'results': results,
        }
        return render(
            request,
            self.template_name,
            context
        )
