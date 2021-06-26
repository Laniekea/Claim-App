from django.urls import path, include
from django.contrib import admin 

from . import views

urlpatterns = [
    path('claims/', include('Claim.urls')),
    path('', views.index, name='index'),
]