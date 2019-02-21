from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nome'}
    ))
    phone = forms.RegexField(r'^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$', label='Telefone', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX'}
    ))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}
    ))
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Mensagem', 'rows': 5, 'cols': 30}
    ))