from django.shortcuts import render, HttpResponse
from blog import signals
# Create your views here.
def home(request):
    signals.notificaion.send(sender=None, request=request, user=['abdl', 'qdr'])
    return HttpResponse("This is Home Page")
    