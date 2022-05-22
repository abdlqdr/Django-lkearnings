from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request, 'fees/fees1.html', {'title': 'fees django', 'cname': 'django wala', 'Fee':3000})
