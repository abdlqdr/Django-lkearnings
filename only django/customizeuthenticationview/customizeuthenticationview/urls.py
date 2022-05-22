"""customizeuthenticationview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.Myhome.as_view(), name='home'),
    path('dashboard/', auth_views.Mydashboard.as_view(), name='dashboard'),
    
    path('login/', auth_views.MyLoginView.as_view(), name='login'),
    path('logout/', auth_views.MyLogoutView.as_view(), name='logout'),
    
    path('changepass/', auth_views.MyPasswordChangeView.as_view(), name='changepass'),
    path('changepassdone/', auth_views.MyPasswordChangeDoneView.as_view(), name='changepassdone'),
    
    path('resetpass/', auth_views.MyPasswordResetView.as_view(), name='resetpass'),
    path('resetpassdone/', auth_views.MyPasswordResetDoneView.as_view(), name='resetpassdone'),
    path('resetpassconfirm/<uidb64>/<token>/', auth_views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('resetpasscomplete/', auth_views.MyPasswordResetCompleteView.as_view(), name='resetpasscomplete'),
    
]
