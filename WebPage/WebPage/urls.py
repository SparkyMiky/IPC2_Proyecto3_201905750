from django.contrib import admin
from django.urls import path, include
from appClient.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appClient/', IndexView.as_view(), name='index' ),
]
