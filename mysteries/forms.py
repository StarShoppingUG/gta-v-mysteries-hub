from django import forms
from .models import Theory

class TheoryForm(forms.ModelForm):
    class Meta:
        model = Theory
        fields = ['title', 'description', 'location', 'image', 'tags']
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
            'tags': forms.TextInput(attrs={
                'placeholder': 'e.g., Mount Chiliad, UFO, Easter Egg',
                'class': 'form-control'
            })
        }