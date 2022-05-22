from django.db.models.query_utils import Q
from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Avg, Sum, Min, Max, Count

# Create your views here.
def home(request):
    # sdata = Student.objects.get(roll=102)
    # sdata = Student.objects.first()
    # sdata = Student.objects.order_by('name').first()
    # sdata = Student.objects.order_by('name').last()
    # sdata = Student.objects.latest('pass_date')
    # sdata = Student.objects.earliest('pass_date')
    # sdata =Student.objects.all()
    # stdata =Student.objects.get(pk=1)
    # print(sdata.filter(pk=stdata.pk).exists())
    # sdata = Student.objects.create(name='Sameer', roll=107, city='Bhuj', marks=67, pass_date='2021-5-4')
    # sdata, created = Student.objects.get_or_create(name='Sameera', roll=108, city='Kharagpur', marks=61, pass_date='2021-5-14')
    # sdata =Student.objects.filter(pk=1).update(name='Kabir', marks=80)
    # sdata = Student.objects.filter(name__exact='Kabir')
    # sdata = Student.objects.filter(name__iexact='kabir')
    # sdata = Student.objects.filter(name__contains='u')
    # sdata = Student.objects.filter(id__in=[1, 5, 7])
    # sdata = Student.objects.filter(marks__lt=80)
    # sdata = Student.objects.filter(name__endswith='l')
    # sdata = Student.objects.filter(pass_date__range=('2021-4-1', '2021-6-1'))
    # sdata = Student.objects.filter(pass_date__month__lte=5)
    # sdata = Student.objects.filter(pass_date__quarter=3)
    # sdata = Student.objects.filter(~Q(id=2))
    # average = sdata.aggregate(Avg('marks'))
    # sum = sdata.aggregate(Sum('marks'))
    # min = sdata.aggregate(Min('marks'))
    # max = sdata.aggregate(Max('marks'))
    # count = sdata.aggregate(Count('marks'))
    # print(average)
    sdata = Student.objects.all()[:10:3]
    # print('SQL Query:', sdata.query)
    return render(request, 'school/home.html', {'students':sdata})