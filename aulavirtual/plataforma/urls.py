from django.conf.urls import url
from django.contrib import admin
from plataforma import views	

urlpatterns = [    
    url(r'^$',views.home,name='home'),
    url(r'^home/$',views.home,name='home'),
    url(r'^cerrar_sesion/$',views.cerrar_sesion,name='cerrar_sesion'),
    url(r'^cursos/$',views.view_cursos,name='cursos'),
    url(r'^cursos/(?P<id_curso>[0-9]+)/$',views.detalle_curso,name='detalle_curso'),    
    url(r'^cursos/form_agregar_curso/$',views.form_agregar_curso,name='form_agregar_curso'),    
    url(r'^cursos/agregar_curso/$',views.agregar_curso,name='agregar_curso'),    
    url(r'^cursos/matricula_alumno_curso/(?P<id_curso>[0-9]+)/$',views.matricula_alumno_curso,name='matricula_alumno_curso'),
    url(r'^mis_cursos/$',views.mis_cursos,name='mis_cursos'),
    url(r'^pagos/$',views.pagos,name='pagos'),    
    url(r'^plataforma/$',views.plataforma,name='plataforma'),
    url(r'^prueba_post/$',views.prueba_post,name='prueba_post'),
    url(r'^profesores/$',views.profesores,name='profesores'),
    url(r'^guardar_progreso/$',views.guardar_progreso,name='guardar_progreso'),
    url(r'^iniciar_sesion/$',views.iniciar_sesion,name='iniciar_sesion'),
    url(r'^registrar_usuario/$',views.registrar_usuario,name='registrar_usuario'),    
    #api
    url(r'^usuarios/$',views.usuarios,name='usuarios'),
    url(r'^courses/$',views.courses,name='courses'),
    url(r'^profesors/$',views.profesors,name='profesors'),
    url(r'^user/(?P<id_user>[0-9]+)/$',views.user,name='user'),
    url(r'^course/(?P<id_course>[0-9]+)/$',views.course,name='course'),
    url(r'^profesor/(?P<id_profesor>[0-9]+)/$',views.profesor,name='profesor'),
]