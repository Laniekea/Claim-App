from claims.forms import AddClaimForm
from django.db.models.base import Model
import Claim
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Claim

def home(request):
    return render(request, 'home.html')

def add_claim(request):
    if request.method == "POST":
        form = AddClaimForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']

            print(username, email, mobile)

    return render(request, 'add_claim.html', {'form' : form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home')

    else: 
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def detail(request, user_id):
    claim = Claim.objects.filter(user_id = user_id)
    return render(request, 'detail.html', {'claim': claim})
