from django.views import View
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.views.generic.base import TemplateView
from .models import Still, Client
from .forms import ContactForm

# Create your views here.

class HomeView(View):
    
    def get(self, request):
        context = {}
        context['stills'] = Still.objects.all()
        context['clients'] = Client.objects.all()
        context['form'] = ContactForm()
        return TemplateResponse(request, 'home.html', context)

    def post(self, request):
        context = {}
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                messages.add_message(request, messages.INFO, 'Obrigado pelo contato!')
                send_mail(
                    'Contato Site Calabouço',
                    'Nome: %s,\nEmail: %s,\nTelefone: %s,\nMensagem: %s' % (
                        form.cleaned_data['name'],
                        form.cleaned_data['email'],
                        form.cleaned_data['phone'],
                        form.cleaned_data['message'],
                    ),
                    'calaboucofilmes@gmail.com',
                    ['calaboucofilmes@gmail.com', 'contato@calaboucofilmes.com']
                )
                return HttpResponseRedirect(reverse('home'))
        except Exception as e:
            messages.add_message(request, messages.INFO, e)
        context['form'] = form
        return TemplateResponse(request, 'home.html', context)

class ProjectView(TemplateView):
    template_name = "still.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['still'] = Still.objects.get(pk=kwargs['still_id'])
        stills = Still.objects.all()
        for i, p in enumerate(stills):
            if p.id == context['still'].id:
                if i != 0:
                    context['prev'] = stills[i-1]
                if i != len(stills) - 1:
                    context['next'] = stills[i + 1]
        return context
