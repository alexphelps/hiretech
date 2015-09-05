from django.shortcuts import render

from django.views.generic import TemplateView

from .forms import CustomSearchForm

class CustomSearchView(TemplateView):
    template_name = 'search/search.html'

    def get(self, request):
        form = CustomSearchForm(request.GET, searchqueryset=None)
        if form.is_valid():
            query = form.cleaned_data['q']
            results = form.search()

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'query': query,
                'results': results,
            }
        )
