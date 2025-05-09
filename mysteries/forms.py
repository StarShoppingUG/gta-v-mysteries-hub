from django import forms
from .models import Theory

class TheoryForm(forms.ModelForm):
    class Meta:
        model = Theory
        fields = ['title', 'description', 'location', 'image', 'author']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter your theory title',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe your theory in detail...',
                'rows': 6,
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Where can this be found in GTA V?',
                'class': 'form-control'
            }),
            'author': forms.TextInput(attrs={
                'placeholder': 'Your username or name',
                'class': 'form-control'
            })
        }