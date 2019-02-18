from django import forms
 
class ContactForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(
        attrs={'class': 'half-form', 'placeholder': 'Nome'}
    ))
    telefone = forms.RegexField(r'\([0-9]{2}\) [0-9]{5}-[0-9]{3,4}_?', label='Telefone', max_length=100, widget=forms.TextInput(
        attrs={'class': 'half-form telephone-number', 'placeholder': 'Telefone'}
    ))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}
    ))
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(
        attrs={'placeholder': 'Mensagem', 'rows': 5, 'cols': 30}
    ))