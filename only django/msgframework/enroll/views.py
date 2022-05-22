from django.contrib.messages.api import get_level
from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.
def regi(request):
    messages.info(request, 'This is blue')
    messages.success(request, 'This is green')
    messages.warning(request, 'This is yello')
    messages.error(request, 'This is error')
    fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})
