from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User

def home(request):
    return render(request, 'home.html')

def add_claim(request):
    return render(request, 'add_claim.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # allow log in
            return redirect("home")

    else: 
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})
