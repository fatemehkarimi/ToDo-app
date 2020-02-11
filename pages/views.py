from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'