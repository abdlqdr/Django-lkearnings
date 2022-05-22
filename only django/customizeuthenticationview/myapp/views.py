from django.shortcuts import render
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView, PasswordChangeDoneView, PasswordChangeView
from .forms import LoginForm
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
class Myhome(TemplateView):
    template_name='myapp/home.html'
    

@method_decorator(login_required, name='dispatch')    
class Mydashboard(TemplateView):
    template_name='myapp/dashboard.html'


class MyLoginView(LoginView):
    template_name='myapp/login.html' 
    authentication_form=LoginForm
    
class MyLogoutView(LogoutView):
    template_name='myapp/logout.html'
    
class MyPasswordChangeView(PasswordChangeView):
    template_name='myapp/changepass.html'
    success_url='/changepassdone/'

class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name='myapp/changepassdone.html'

class MyPasswordResetView(PasswordResetView):
    template_name='myapp/resetpass.html'
    success_url='/resetpassdone/'
    
class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name='myapp/resetpassdone.html'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name='myapp/resetpassconfirm.html'
    success_url='/resetpasscomplete/'

class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name='myapp/resetpasscomplete.html'