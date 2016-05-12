from django import forms
from django.contrib.auth.models import User
from .models import Curso

class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
		fields = '__all__'

class RegUsForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","email","password"]		