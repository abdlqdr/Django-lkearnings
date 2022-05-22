from django.contrib import admin
from .models import user

# Register your models here.

@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'teacher_name', 'email', 'password']