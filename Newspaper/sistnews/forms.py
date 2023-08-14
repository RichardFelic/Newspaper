from tkinter import Widget
from django import forms
from .models import Clasificacion, Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__' 
        widgets = {
            'fecha': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            'epigrafe':forms.TextInput(attrs={'class':'form-control'}),
            'titular': forms.TextInput(attrs={'class':'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control'}),
            'imagen':forms.FileInput(attrs={'class':'form-control', 'type':'file'}),
            'piefoto':forms.TextInput(attrs={'class':'form-control'}),
            'clasificacion': forms.Select(attrs={'class':'form-select'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']