from django.shortcuts import render

# Create your views here.
# def home(request, check):
#     print(check)
#     return render(request, 'enroll/home.html', {'ch': check})


def show_detail(request, year):    
    student={'yr':year}
    return render(request, 'enroll/show.html', student)

