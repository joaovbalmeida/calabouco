from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nome'}
    ))
    phone = forms.CharField(label='Telefone', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Telefone'}
    ))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}
    ))
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 12, 'cols': 30}
    ))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['message'].initial = '''Olá, 
(responda esse breve briefing e nos ajude a acelerar o seu orçamento)

Sobre o que é o seu projeto?
Qual o seu objetivo com esse filme, o que você pretende alcançar?
Onde o vídeo será exibido?
Qual o prazo para a entrega do filme?
Você tem algum planejamento prévio de filmagem?
Haverá captação de som? E trilha sonora original?

Aguardo o contato,
(assinado)'''