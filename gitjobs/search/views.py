from django.shortcuts import render

from django.views.generic import TemplateView

from .forms import CustomSearchForm
from jobs.models import Job

class CustomSearchView(TemplateView):
    template_name = 'search/search.html'

    def get(self, request):
        query = ''
        results = []
        filtered_results = []
        form = CustomSearchForm(request.GET, searchqueryset=None)
        if form.is_valid():
            query = form.cleaned_data['q']
            results = form.search()
            for each in results:
                if each.object.job_status == 'published':
                    filtered_results.append(each)

        context = {
            'form': form,
            'query': query,
            'results': filtered_results,
        }
        return render(
            request,
            self.template_name,
            context
        )
