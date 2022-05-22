from django.contrib import admin
from .models import Construction, Student, Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'fees']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date', 'salary']

@admin.register(Construction)
class ConstructionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date', 'payment']
