from django import forms

from haystack.forms import SearchForm,ModelSearchForm

class CustomSearchForm(SearchForm):
    q = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'search-input',
                'placeholder': 'Filter by title, benefits, companies',
            }),
        )
    def search(self):
        if not self.is_valid():
            return self.no_query_found()
        if not self.cleaned_data.get('q'):
            return self.no_query_found()
            
        query = self.cleaned_data['q']
        sqs = self.searchqueryset.auto_query(query)
        return sqs
