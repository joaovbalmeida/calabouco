from django.views import View
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from .models import Still, Client

# Create your views here.

class HomeView(View):
    
    def get(self, request):
        context = {}
        context['stills'] = Still.objects.all()
        context['clients'] = Client.objects.all()
        return TemplateResponse(request, 'home.html', context)