from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserAddShowView.as_view(), name='addshow'),
    path('<int:id>/', views.UserUpdateView.as_view(), name='updatedata'),
    path('delete/<int:id>/', views.UserDeleteView.as_view(), name='deletedata'),

]