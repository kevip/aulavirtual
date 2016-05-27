from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core import serializers

from .forms import CursoForm, RegUsForm
from .models import Curso,Profesor,Alumno
import json
# Create your views here.

def home(request):
	if request.user.is_authenticated():		
		return render(request,"plataforma/home.html",{})
	else:
		form = RegUsForm()
		return render(request,"plataforma/home.html",{
			'form' : form,
			})

def cursos(request):	
	cursos = Curso.objects.all()	
	template = loader.get_template("plataforma/cursos.html")
	context = {
		"cursos": cursos
	}
	return HttpResponse(template.render(context,request))
	
def form_agregar_curso(request):		
	form = CursoForm()		
	return render(request,"plataforma/form_agregar_curso.html",{
		"form": form,
		})

def agregar_curso(request):
	if request.method == 'POST':
		form = CursoForm(request.POST, request.FILES)
		if form.is_valid():
			curso = form.save()
			curso.save()
			return HttpResponseRedirect("/cursos")
		else:
			return HttpResponseRedirect("/cursos")			
	else:
		return HttpResponseRedirect("/home")			


def detalle_curso(request, id_curso):	
	curso = get_object_or_404(Curso,id=id_curso)		
	template = loader.get_template("plataforma/detalle_curso.html")
	context = {
		"curso": curso
	}
	return HttpResponse(template.render(context,request))

def iniciar_sesion(request):
	if request.method == "POST":		
		email = request.POST.get('email',None)
		password = request.POST.get('password',None)						
		try:			
			user_e = User.objects.get(email=email)
		except User.DoesNotExist:
			user_e = None

		user = authenticate(username=user_e, password=password)		

		if not user_e:			
			return HttpResponse("<h1>no existe usuario<a href='/'>Volver</a></h1>")
		elif user is not None:
			if user.is_active:
				login(request,user)
		else:
			return HttpResponse("<h1>no se pudo autenticar<a href='/'>Volver</a></h1>")
	return HttpResponseRedirect('/')

def cerrar_sesion(request):
	logout(request)
	
	return HttpResponseRedirect('/')

def registrar_usuario(request):
	if request.method == "POST":		
		action = request.POST.get('action',None)
		nombre = request.POST.get('first_name',None)
		apellido = request.POST.get('last_name',None)
		email = request.POST.get('email',None)
		password = request.POST.get('password',None)		 
	
		existe_usuario = User.objects.filter(email=email)
		if not existe_usuario:			
			usuario = User(first_name=nombre, last_name=apellido, email=email)			
			usuario.username = nombre+" "+apellido
			usuario.set_password(password)
			usuario.is_superuser = False
			usuario.save()			
			
			alumno = Alumno(user_id=usuario.id)
			alumno.save()
			
			return HttpResponse("<h1>Se registro Alumno con exito <a href='/'>Volver</a></h1>")			
		else:
			return HttpResponse("<h1>El usuario ya existe</h1>")		
	return HttpResponseRedirect('/')
	#return render(request,"plataforma/home.html",{})
def usuarios(request):
	usuarios = User.objects.all()
	usuarios = serializers.serialize('json',usuarios)
	return HttpResponse(usuarios,content_type="application/json")

def prueba_post(request):	
	if request.method =="POST":
		response_data = {}				
		name = request.POST.get('name')

        #post = Post(text=post_text, author=request.user)
        #post.save()

		response_data['result'] = 'Create post successful!'        
		response_data['name'] = name
		
		#data = serializers.serialize('json',response_data)		
		return HttpResponse(json.dumps(response_data),content_type="application/json")

def plataforma(request):
	return render(request,"plataforma/plataforma.html",{})

def pagos(request):
	return render(request,"plataforma/pagos.html",{})

def profesores(request):
	profesores = Profesor.objects.all()
	
	return render(request,"plataforma/profesores.html",{
		'profesores':profesores,
		})

def mis_cursos(request):
	cursos = Curso.objects.all()	
	template = loader.get_template("plataforma/mis_cursos.html")
	context = {
		"cursos": cursos
	}
	return HttpResponse(template.render(context,request))

def guardar_progreso(request):
	if request.method == "POST":
		#response.data ={}
		termino_video = request.POST.get("termino_video")
		return HttpResponse("<p>"+termino_video+"</p>")
		#if(termino_video):
		#	return HttpResponse("")

def matricula_alumno_curso(request, id_curso):	
	curso = get_object_or_404(Curso,id=id_curso)
	cursos = Curso.objects.all()
	template = loader.get_template("plataforma/detalle_curso.html")	
	form = CursoForm()		
	return render(request,"plataforma/matricula.html",{
		"form": form,
		"curso":curso,
		"cursos":cursos,
		})	