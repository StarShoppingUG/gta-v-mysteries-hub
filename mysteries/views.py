from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from .forms import TheoryForm
from .models import Theory, Developer

def home(request: HttpRequest):
    context = {
        'title': 'Welcome to GTA V Mysteries Hub',
        'hero_text': 'Explore Hidden Mysteries and Codes',
        'page_description': 'Your ultimate source for GTA V mysteries and secrets'
    }
    return render(request, 'home.html', context)

def browse(request):
    mysteries = Theory.objects.all().order_by('-created_at')
    context = {
        'title': 'Browse Mysteries & Cheats',
        'page_description': 'Explore GTA V mysteries and cheat codes',
        'mysteries': mysteries,
        'cheats': {
            'pc': [],
            'xbox': [],
            'ps': []
        }
    }
    return render(request, 'browse.html', context)

def create(request):
    if request.method == 'POST':
        form = TheoryForm(request.POST, request.FILES)
        if form.is_valid():
            theory = form.save(commit=False)
            theory.author = request.user
            theory.save()
            return redirect('profile')
    else:
        form = TheoryForm()
    return render(request, 'create.html', {'form': form})

def profile(request):
    users = User.objects.all()
    context = {
        'title': 'User Profiles',
        'users': users
    }
    return render(request, 'profile.html', context)

def about(request):
    developers = Developer.objects.all()
    context = {
        'developers': developers,
    }
    return render(request, 'about.html', context)