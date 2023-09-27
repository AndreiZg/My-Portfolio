from django import forms
from django.core.validators import validate_email


class ContactForm(forms.Form):
    email = forms.EmailField(required=True, max_length=255, validators=[validate_email],
                             widget=forms.TextInput({"type": "email"}))
    subject = forms.CharField(required=True, max_length=255,
                              widget=forms.TextInput({"type": "text"}))
    message = forms.CharField(required=True, max_length=10 ** 4,
                              widget=forms.Textarea(
                                  attrs={"cols": 30, "rows": 10}))
