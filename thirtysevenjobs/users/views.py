from django.shortcuts import render_to_response,redirect
from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.contrib.messages import constants as MSG
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseRedirect,
)

from .forms import SignupForm, LoginForm, PasswordResetRequestForm
from .models import UserProfile
from jobs.models import Job
from companies.models import Company

# Create your views here.
class LogoutView(TemplateView):
    def get(self,request):
        logout(request)
        info_msg = 'You have been logged out.'
        messages.add_message(
            self.request,
            MSG.SUCCESS,
            info_msg
        )
        return HttpResponseRedirect(
            reverse('login')
        )


class LoginView(TemplateView):
    template_name = 'login.html'
    def get(self,request):
        form = LoginForm()
        context = {
            'form':form,
        }
        return render(
            request,
            self.template_name,
            context
        )
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('dashboard')
                    )
            else:
                error_msg = 'Your email and password do not match. Please try again.'
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

class ResetPasswordRequestView(TemplateView):
    template_name = 'password-reset.html'
    def get(self,request):
        form = PasswordResetRequestForm()
        context = {
            'form':form,
        }
        return render(
            request,
            self.template_name,
            context
        )
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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            company_name = form.cleaned_data['company_name']
            company_url = form.cleaned_data['company_url']
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
            username = form.cleaned_data['email']
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
        current_user_company = current_user_profile.company.id
        current_user_company_jobs = Job.objects.filter(job_company=current_user_company)
        context = {
            'current_user_profile':current_user_profile,
            'current_user_company_jobs':current_user_company_jobs,
        }
        return render(
            request,
            self.template_name,
            context
        )
