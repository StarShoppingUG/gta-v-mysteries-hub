from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .forms import CustomUserCreationForm, PasswordResetForm
from .forms import TheoryForm
from .models import Theory, Developer, CheatCode
from django.contrib import messages
from django.http import JsonResponse, HttpResponseNotAllowed

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def home(request: HttpRequest):
    context = {
        'title': 'Welcome to GTA V Mysteries Hub',
        'hero_text': 'Explore Hidden Mysteries and Codes',
        'page_description': 'Your ultimate source for GTA V mysteries and secrets'
    }
    return render(request, 'home.html', context)

def browse(request:HttpRequest):
    mysteries = Theory.objects.filter(category='team').order_by('-created_at')
    com_mysteries = Theory.objects.filter(category = 'community', is_approved = True).order_by('-created_at')
    cheats = CheatCode.objects.filter(platform = "ps")
    context = {
        'cheats' : cheats,
        'mysteries' : mysteries,
        'com_mysteries' : com_mysteries
        }   
    return render(request, 'browse.html', context)

def create(request:HttpRequest):
    if request.method == 'POST':
        form = TheoryForm(request.POST, request.FILES)
        if form.is_valid():
            theory = form.save(commit=False)
            if request.user.is_authenticated:
                theory.username = request.user.username
            else:
                theory.username = 'Guest'
            theory.save()
            return redirect('profile')
    else:
        form = TheoryForm()
    return render(request, 'create.html', {'form': form})

def profile(request:HttpRequest):
    if request.user.is_authenticated:
        mysteries = Theory.objects.filter(username = request.user.username, category ="community")
    else:
        mysteries = Theory.objects.filter(username = 'Guest', category ="community")
    
    context = {
        'user': request.user,
        'mysteries': mysteries
    }
    return render(request, 'profile.html', context)

def about(request:HttpRequest):
    developers = Developer.objects.all()
    context = {
        'developers': developers,
    }
    return render(request, 'about.html', context)

def filter_cheats(request:HttpRequest):
    platform = request.GET.get("platform")
    cheats = CheatCode.objects.filter(platform = platform)
    context = {"cheats": cheats}
    return render(request, "platform-cheats.html", context)


def delete_mystery(request:HttpRequest, id:int):
    if request.method == 'POST':
        try:
            mystery = Theory.objects.get(pk=id)
            mystery.delete()
            return JsonResponse({"success" : True})
        except mystery.DoesNotExist:
            return JsonResponse({"success": False, "error": "Not found"}, status=404)

    return HttpResponseNotAllowed(['POST'])

def edit_mystery(request:HttpRequest, id:int):
    mystery = get_object_or_404(Theory, pk=id)
    if request.method == 'POST':
        form = TheoryForm(request.POST, request.FILES, instance= mystery)
        if form.is_valid():
            mystery.is_approved = False
            form.save()
            return redirect("profile")
    else:
        form = TheoryForm(instance=mystery)
    return render(request, "create.html", {'form' : form})

def register(request:HttpRequest):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

def reset_password_start(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return redirect('reset_form', username=username)
        else:
            messages.error(request, "Account does not exist.")
    return render(request, 'reset_username.html')


def reset_password_form(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('reset_start')

    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user.password = make_password(form.cleaned_data['new_password'])
            user.save()
            messages.success(request, "Password updated. You can now log in.")
            return redirect('login')
    else:
        form = PasswordResetForm()

    return render(request, 'reset_form.html', {'form': form, 'username': username})
