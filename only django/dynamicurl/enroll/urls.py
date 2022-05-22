
from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
urlpatterns = [
   
    path('session/<yyyy:year>/', views.show_detail, name="detail"),
    # path('<int:my_id>/<int:my_sid>/', views.show_detail1, name="detail1"),
]
