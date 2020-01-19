from django import forms
from django.forms import ModelForm

from .models import *

class AlumnoForm(forms.ModelForm):
	dni= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ingrese DNI...'}))
	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese los nombres...'}))
	apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese los apellidos...'}))
	class Meta:
		model = Alumno
		fields = '__all__'
