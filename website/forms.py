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
        attrs={'class': 'form-control', 'placeholder': 'Mensagem', 'rows': 5, 'cols': 30}
    ))