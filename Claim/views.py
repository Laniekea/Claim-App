from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User

def index(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # allow log in
            return redirect('index')

    else: 
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})