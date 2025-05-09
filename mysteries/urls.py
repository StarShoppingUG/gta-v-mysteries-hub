from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse, name='browse'),
    path('create/', views.create, name='create'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('filter-cheats/', views.filter_cheats, name='filter-cheats'),
    path('delete-mystery/<int:id>', views.delete_mystery, name="delete_mystery"),
    path('edit-mystery/<int:id>', views.edit_mystery, name="edit_mystery")
]