from django.urls import path
from .views import *


urlpatterns = [
    path('creadores/', ListarCreadores.as_view(),
    		name = "listar_creadores"),
    path('creadores/agregar', agregar_creador(),
    		name = "agregar_creador_url"),
    path('publicaciones/', ListarPublicaciones.as_view(),
    		name = "listar_publicaciones"),
    path('publicaciones/agregar', agregar_publicaciones,
    		name = "agregar_publicacion_url"),
    path('comentarios/<id_publicacion>',
    		ListarComentarios.as_view(),
    		name = "listar_comentarios"),
    path('comentarios/<id_publicacion>',
    		agregar_comentario,
    		name = "agregar_comentario_url"),
]