from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(required=True, max_length=255,
                             widget=forms.TextInput())
    subject = forms.CharField(required=True, max_length=255)
    message = forms.Textarea(deffault_attrs)

