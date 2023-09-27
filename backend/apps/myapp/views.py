from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.views import View
from django.conf import settings

from .forms import ContactForm


class ContactView(View):
    form_class = ContactForm
    template_name = "apps.myapp/contact.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            messages.success(request,
                             message='Email has been sent successfully!')
            send_mail(
                subject="Contact me",
                message=f"From: {request.POST['email']}\n\nSubject: {request.POST['subject']}\n\n" +
                        f"Message: {request.POST['message']}\n",
                from_email=settings.FROM_EMAIL,
                recipient_list=[settings.RECIPIENT_EMAIL],
                fail_silently=False
            )
            return redirect("contact")

        messages.error(request, message="Ops... Check the data you entered and try again!")

        return render(request, self.template_name, {'form': form})
