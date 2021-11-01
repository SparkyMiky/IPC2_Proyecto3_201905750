from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs ):
        return super(IndexView, self).get_context_data(**kwargs)

