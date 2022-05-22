from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('learndj/', views.learn_django)
]
