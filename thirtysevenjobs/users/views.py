from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.contrib.messages import constants as MSG
from django.core.mail import send_mail
from django.db.models.query_utils import Q
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseRedirect,
)
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render_to_response,redirect
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView


from .forms import SignupForm, LoginForm, PasswordResetRequestForm, PasswordResetNewPassword
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
    def post(self,request):
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            associated_users= User.objects.filter(Q(username=username))
            if associated_users.exists():
                for user in associated_users:
                    c = {
                        'email': user.email,
                        'domain': request.META['HTTP_HOST'],
                        'site_name': 'your site',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                        }
                    subject_template_name='registration/password_reset_subject.txt'
                    email_template_name='registration/password_reset_email.html'
                    subject = loader.render_to_string(subject_template_name, c)
                    subject = ''.join(subject.splitlines())
                    email = loader.render_to_string(email_template_name, c)
                    send_mail(subject, email, 'alexphelps3@gmail.com' , [user.email], fail_silently=False)
                    success_msg = 'A confirmation email has been sent to ' + username
                    success_msg += '. Please follow the link in the email to reset your password.'
                    messages.add_message(
                        self.request,
                        MSG.SUCCESS,
                        success_msg
                    )
            else:
                error_msg = 'Your email does not exist in the system.'
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

class PasswordResetConfirmView(TemplateView):
    template_name = 'password-reset-confirm.html'
    def get(self,request, uidb64=None, token=None, *arg, **kwargs):
        form = PasswordResetNewPassword()
        context = {
            'form':form,
        }
        return render(
            request,
            self.template_name,
            context
        )
    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        UserModel = get_user_model()
        form = PasswordResetNewPassword(request.POST)
        assert uidb64 is not None and token is not None  # checked by URLconf
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                password1 = form.cleaned_data.get('new_password')
                password2 = form.cleaned_data.get('new_password2')
                if password1 != password2:
                    error_msg = 'Passwords do not match.'
                    messages.add_message(
                        self.request,
                        MSG.ERROR,
                        error_msg
                    )
                else:
                    user.set_password(password2)
                    user.save()
                    success_msg = 'Your password has been reset. You can now log in below.'
                    messages.add_message(
                        self.request,
                        MSG.SUCCESS,
                        success_msg
                    )
                    return HttpResponseRedirect(
                        reverse('login')
                    )
            else:
                error_msg = 'Password reset has not been unsuccessful.'
                messages.add_message(
                    self.request,
                    MSG.ERROR,
                    error_msg
                )
        else:
            error_msg = 'The reset password link is no longer valid.'
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
