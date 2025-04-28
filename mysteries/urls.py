from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse, name='browse'),
    path('create/', views.create, name='create'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
]
