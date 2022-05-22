"""baseview URL Configuration

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

from re import template
from django.contrib import admin
from django.urls import path
from school import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', views.myview, name='func'),
    # path('cl/', views.MyView.as_view(), name='cl'),
    path('cl/', views.MyView.as_view(name='Rahul'), name='cl'),
    path('subcl/', views.MyViewChild.as_view(), name='subcl'),
    path('newsfun/', views.newsfun, {'template_name':'school/news2.html'}, name='newsfun'),
    path('newsfuncl/', views.newsfunclass.as_view( template_name = 'school/news2.html' ), name='newsfuncl'),
]
