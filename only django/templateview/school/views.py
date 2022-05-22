from re import template
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.

# class HomeTemplateView(TemplateView):
#     template_name = 'school/home.html'
    
#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         context['name'] = 'Sonam'
#         context['roll'] = 101
#         # context = {'name': 'Sonam', 'roll': 101}
#         return context

class googleRedirectView(RedirectView):
    url = 'https://www.google.com'

class googRedirectView(RedirectView):
    pattern_name = 'googx'
    permanent = True
    query_string = True