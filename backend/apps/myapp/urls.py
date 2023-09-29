from django.urls import path
from django.views.generic import TemplateView

from .views import ContactView

urlpatterns = [
    path('', TemplateView.as_view(template_name="apps.myapp/welcome.html"), name='welcome'),
    path('about/', TemplateView.as_view(template_name="apps.myapp/about.html"), name='about'),
    path('projects/', TemplateView.as_view(template_name="apps.myapp/projects.html"), name='projects'),
    path('contact/', ContactView.as_view(), name='contact')

]
