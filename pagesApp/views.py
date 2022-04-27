#from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'
    
    #def get(self, request, *args, **kwargs):
    #    messages.debug(request, 'Debug message')
    #    messages.info(request, 'info message')
    #    messages.success(request, 'success message')
    #    messages.warning(request, 'warning message')
    #    messages.error(request, 'error message')
    #    return super().get(request, args, kwargs)


# Create your views here.
