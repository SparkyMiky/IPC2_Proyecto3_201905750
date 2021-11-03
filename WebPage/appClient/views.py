from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import requests

endpoint = 'http://localhost:5000{}'

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        docs = request.FILES['archivoInput']
        data = docs.read()
        url = endpoint.format('/appClient')
        requests.post(url, data)
        
        url = endpoint.format('/appClient')
        data = requests.get(url)
        context = {
            'datos' : data.text,
            'data': data.text,
        }
        
        return render(request, 'index.html', context)


