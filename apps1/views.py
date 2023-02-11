from django.shortcuts import render
from django.views import generic

class LandingPage(generic.TemplateView):
    template_name = "apps1/index.html"
