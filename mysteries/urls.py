from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('home/', views.home, name='home'),
    path('browse/', views.browse, name='browse'),
    path('create/', views.create, name='create'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('filter-cheats/', views.filter_cheats, name='filter-cheats'),
    path('delete-mystery/<int:id>', views.delete_mystery, name="delete_mystery"),
    path('edit-mystery/<int:id>', views.edit_mystery, name="edit_mystery"),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', views.register, name="register"),
    path('reset-password/', views.reset_password_start, name='reset_start'),
    path('reset-password/<str:username>/', views.reset_password_form, name='reset_form'),
]