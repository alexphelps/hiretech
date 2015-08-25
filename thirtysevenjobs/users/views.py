from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SignupForm

# Create your views here.
class SignupView(TemplateView):
    template_name = 'signup.html'
    def get(self,request):
        form = SignupForm()
        context = {
            'form':form,
        }
        return render(
            request,
            self.template_name,
            context
        )

    def post(self,request):
        form = SignupForm(request.POST)
        if form.is_valid():
            print request.POST
        else:
            print 'no'
        context = {
            'form':form,
        }
        return render(
            request,
            self.template_name,
            context
        )
