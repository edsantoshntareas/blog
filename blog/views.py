from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .models import *


class ListarCreadores(generic.ListView):
	template_name = 'creador/index.html'
	context_object_name = 'creadores_contexto'

	def get_queryset(self):
		return Creador.objects.all()


def agregar_creador(request):
	if request.method == "post":
		form = NuevoCreadorForm(request.POST)
		if form.is_valid():
			obj = Creador()
			obj.nombre = form.cleaned_data['nombre']
			obj.email = form.cleaned_data['email']
			obj.save()
			return HttpResponseRedirect(reverse(
				'blog:listar_creadores'))
	else:
		form = NuevoCreadorForm()
	return render(request, 'creador/agregar.html', 
					{'form': form})


class ListarPublicaciones(generic.ListView):
	template_name = 'publicaciones/index.html'
	context_object_name = 'publicaciones_contexto'

	def get_queryset(self):
		return Publicacion.objects.all()

def agregar_publicacion(request):
	if request.method == "post":
		form = NuevaPublicacionForm(request.POST)
		if form.is_valid():
			obj = Publicacion()
			obj.titulo = form.cleaned_data['titulo']
			obj.descripcion = form.cleaned_data['descripcion']
			obj.creador = form.cleaned_data['creador']
			obj.save()
			return HttpResponseRedirect(reverse(
					'blog:listar_publicaciones'))
	else:
		form = NuevaPublicacionForm()
	return render(request, 'publicaciones/agregar.html',
					{'form': form})


class ListarComentarios(generic.ListView):
	template_name = 'comentarios/index.html'
	context_object_name = 'comentarios_contexto'

	def get_queryset(self):
		return Comentario.objects.all()


def agregar_comentario(request, id_publicacion):
	if request.method == 'post':
		form = NuevoComentarioForm(request.POST)
		if form.is_valid():
			obj = Comentario()
			obj.nombre_usuario = form.cleaned_data['nombre_usuario']
			obj.descripcion = form.cleaned_data['descripcion']
			obj.publicacion = id_publicacion
			obj.puntuacion = form.cleaned_data['puntuacion']
			obj.save()
			return HttpResponseRedirect(reverse(
						'blog:ver_publicacion' arg = [id_publicacion]))
	else:
		form = NuevoComentarioForm()
	return render(request, 'comentarios/agregar.html',
					{'form':form})
	