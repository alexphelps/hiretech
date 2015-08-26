from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.models import User

from .forms import SignupForm
from .models import UserProfile
from companies.models import Company

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
        form = SignupForm(request.POST,request.FILES)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            company_name = request.POST['company_name']
            company_url = request.POST['company_url']
            company_logo = request.FILES['company_logo']
            print request.FILES
            user = User.objects.create_user(
                username=email,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            company = Company.objects.create(
                company_name=company_name,
                company_url=company_url,
                company_logo=company_logo
            )
            UserProfile.objects.create(
                user=user,
                company=company
            )
            print request.POST
        else:
            print form.errors
        context = {
            'form':form,
        }
        return render(
            request,
            self.template_name,
            context
        )
