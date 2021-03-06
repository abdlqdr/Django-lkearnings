from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setcookies(request):
    response = render(request, 'student/setcookie.html')
    response.set_signed_cookie('name', 'Sonam', salt='nm', expires=datetime.utcnow()+timedelta(days=2))
    return response

def getcookies(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name')
    name = request.get_signed_cookie('name', default='Guest', salt='nms')
    return render(request, 'student/getcookie.html', {'name':name})

def delcookies(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    return response