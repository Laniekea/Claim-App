from django.urls import path, include
from django.contrib import admin 
from django.views.generic.base import TemplateView 
from . import views


app_name = 'claim'

urlpatterns = [

    path('signup', views.signup, name="signup"),
    path('', views.home, name="home"),
    path('claims/<int:user_id>/', views.detail, name="detail"),
    path('claims/add', views.add_claim, name="add_claim"),
    
]