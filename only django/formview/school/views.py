
from django.shortcuts import render, HttpResponse
from .forms import ContactForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

# Create your views here.
class ContactFormView(FormView):
    template_name = 'school/contact.html'
    form_class = ContactForm
    success_url = '/thankyou/'
    initial = {'name': 'abdl', 'email':'qdr@fm.cm'}
    
    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        return super().form_valid(form)
        # return HttpResponse('Msg Sent')
    
class ThanksTemplateview(TemplateView):
    template_name = 'school/thankyou.html'
    