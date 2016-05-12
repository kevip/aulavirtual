from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from .models import Profesor, Curso, Alumno


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):

    list_display = ('id',User,)
    #list_filter = ('User',)
    search_fields = ('nombre',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):

    list_display = ('id','nombre', 'codigo', 'profesor', 'logo',)
    list_filter = ('profesor',)
    search_fields = ('nombre',)

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):

	list_display = ('id',User,)
	search_fields = ('nombre',)