from django import forms
from django.contrib.auth.models import User
from .models import Curso

class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
		fields = '__all__'		
		widgets = {
			'nombre': forms.TextInput(
			 	attrs = { 'class' : 'validate', 
			 			'required' : True}
			),
			'codigo': forms.TextInput(
			 	attrs = { 'class' : 'validate', 
			 			'required' : True}
			),
			'logo': forms.FileInput(
			 	attrs = { 'required' : True}
			),
			'descripcion': forms.Textarea(
				attrs = { 'class' : 'descripcion materialize-textarea',
						'required' : True}
			),
		}

class RegUsForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","email","password"]
		widgets = {
			'first_name': forms.TextInput(
			 	attrs = { 'class' : 'validate',			 			
			 			'required' : True},
			),
			'last_name': forms.TextInput(
			 	attrs = { 'class' : 'validate', 
			 			'required' : True}
			),
			'email': forms.EmailInput(
			 	attrs = { 'class' : 'validate',
			 			'required' : True}
			),
			'password': forms.PasswordInput(
				attrs = { 'class' : 'validate',
						'required' : True}
			),
		}
