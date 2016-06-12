from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core import serializers

from .forms import CursoForm, RegUsForm
from .models import Curso,Profesor,Alumno
import json


def cursos(request):
	usuarios = Curso.objects.all()
	usuarios = serializers.serialize('json',usuarios)
	return HttpResponse(usuarios,content_type="application/json")