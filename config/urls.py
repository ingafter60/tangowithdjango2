# confit/urls.py
from django.contrib import admin
from django.urls import path
from django.urls import include

from rango import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
