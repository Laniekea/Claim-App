from django.urls import path, include
from django.contrib import admin 

from . import views


app_name = 'Claim'

urlpatterns = [

    #path('claims/', include('Claim.urls')),
    path('signup', views.signup_view, name="signup"),
    path('login', views.login_view, name="login"),
    path('', views.index, name='index'),
    
]