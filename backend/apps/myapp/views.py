from django.shortcuts import render
from django.views.generic import FormView

from .forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm
    template_name = "apps.myapp/contact.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        pass
