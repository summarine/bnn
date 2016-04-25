from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Template,Context
from django.shortcuts import render_to_response
from django.views import generic
class HomePageView(generic.ListView):
    #indexHtml = loader.get_template('static/base.html')
    template_name='forecasting/index.html'
    
    def get_queryset(self):
        return 0
