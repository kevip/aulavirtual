from django.conf.urls import url
from django.contrib import admin
from plataforma import views	

urlpatterns = [    
    url(r'^$',views.home,name='home'),
    url(r'^home/$',views.home,name='home'),
    url(r'^cursos/$',views.cursos,name='cursos'),
    url(r'^cursos/(?P<id_curso>[0-9]+)/$',views.detalle_curso,name='detalle_curso'),    
    url(r'^cursos/form_agregar_curso/$',views.form_agregar_curso,name='form_agregar_curso'),    
    url(r'^cursos/agregar_curso/$',views.agregar_curso,name='agregar_curso'),    
    url(r'^iniciar_sesion/$',views.iniciar_sesion,name='iniciar_sesion'),
    url(r'^cerrar_sesion/$',views.cerrar_sesion,name='cerrar_sesion'),
    url(r'^registrar_usuario/$',views.registrar_usuario,name='registrar_usuario'),    
]