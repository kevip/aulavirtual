from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django import forms


class Profesor(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)	
	
	class Meta:
		verbose_name_plural="Profesores"

	def __str__(self):
		return self.user

class Curso(models.Model):

	nombre = models.CharField('Nombre',max_length=100)
	codigo = models.CharField('Codigo',max_length=100)
	logo = models.ImageField('Logo', upload_to='cursos/logos/')
	profesor = models.ForeignKey('Profesor',on_delete=models.CASCADE)

	class Meta:
		verbose_name='Curso'
		verbose_name_plural = "Cursos"
	def __str__(self):
		return self.nombre	

class Alumno(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.get_full_name()		

class Matricula(models.Model):
	fecha_matricula = models.DateField()
	alumno = models.ForeignKey('Alumno')
	curso = models.ForeignKey('Curso')

class Membresia(models.Model):
	tipo_membresia = models.CharField('Tipo',max_length=100)
	costo = models.DecimalField(max_digits=5,decimal_places=2)

class Acceso(models.Model):
	fecha_inicio = models.DateField()
	fecha_final = models.DateField()
	terminado = models.BooleanField(default=False)
	membresia = models.ForeignKey('Membresia')
	alumno = models.ForeignKey('Alumno')
