from django.contrib import admin
from django.urls import path, include
from werkzeug.wrappers import request
from appClient.views import *

urlpatterns = [
    path('', index),
]
