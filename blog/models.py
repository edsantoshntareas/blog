from django.db import models
import uuid 


class Creador(models.Model):
	nombre = models.CharField(max_length = 45,
				help_text = "Escriba el nombre")
	email = models.EmailField(help_text = "Escriba el Email")

	def __str__(self):
		return self.nombre


class Publicacion(models.Model):
	titulo = models.CharField(max_length = 100,
				help_text = "Escriba el Titulo de la entrada")
	descripcion = models.CharField(max_length = 4000,
				help_text = "Escriba la entrada")
	fecha_pub = models.DateField(auto_now = True)
	creador = models.ForeignKey(Creador,
				help_text = "Seleccione el Creador",
				on_delete = models.CASCADE)

	def __str__(self):
		return "%s %s %s" % (self.titulo, self.creador, 
								self.fecha_pub)


class Comentario(models.Model):
	nombre_usuario = models.CharField(max_length = 30)
	fecha_com = models.DateField(auto_now = True)
	descripcion = models.CharField(max_length = 1000)
	publicacion = models.ForeignKey(Publicacion,
				on_delete = models.CASCADE)
	puntuacion = models.IntegerField()

	def __str__(self):
		return self.descripcion