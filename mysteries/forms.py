from django import forms
from .models import Theory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help text for all fields
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None

class PasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        data = self.cleaned_data
        if data.get('new_password') != data.get('confirm_password'):
            raise forms.ValidationError("The password fields didn't match.")
        return data
