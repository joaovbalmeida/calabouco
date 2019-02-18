from django.views import View
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Still, Client
from .forms import ContactForm

# Create your views here.

class HomeView(View):
    
    def get(self, request):
        context = {}
        context['stills'] = Still.objects.all()
        context['clients'] = Client.objects.all()
        return TemplateResponse(request, 'home.html', context)

    def post(self, request):
        context = {}
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                messages.add_message(request, messages.INFO, 'Obrigado pelo contato!')
                send_mail(
                    'Contato Site Calabouço',
                    'Nome: %s, Email: %s, Telefone: %s, Mensagem: %s' % (
                        form.cleaned_data['nome'],
                        form.cleaned_data['email'],
                        form.cleaned_data['telefone'],
                        form.cleaned_data['mensagem'],
                    ),
                    settings.EMAIL_HOST_USER,
                    ['joaovbalmeida@gmail.com']
                )
                return HttpResponseRedirect(reverse('home'))
        except Exception as e:
            messages.add_message(request, messages.INFO, 'Não conseguimos enviar a mensagem, por favor tente novamente.')
        context['form'] = form
        return TemplateResponse(request, 'home.html', context)