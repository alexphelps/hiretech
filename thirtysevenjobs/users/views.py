from django.shortcuts import render_to_response,redirect
from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.models import User
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseRedirect,
)
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages import constants as MSG

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
            #log them in if we were able to sign them up
            username = request.POST['email']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
        else:
            error_msg = 'Ooops, please see required fields below.'
            messages.add_message(
                self.request,
                MSG.ERROR,
                error_msg
            )

        context = {
            'form':form,
        }
        return render(
            request,
            self.template_name,
            context
        )

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    def get(self,request):
        current_user = request.user
        current_user_id = current_user.id
        current_user_profile = UserProfile.objects.get(user__id=current_user_id)
        context = {
            'current_user_profile':current_user_profile,
        }
        return render(
            request,
            self.template_name,
            context
        )
