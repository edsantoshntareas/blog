from django import forms


class NuevoCreadorForm(forms.Form):
	nombre = forms.CharField(label = "Nombre",
				max_length = 45,
				help_text = "Escriba el nombre")
	email = forms.EmailField(label = "Email",
				placeholder = "Escriba el Email")


class NuevaPublicacionForm(forms.Form):
	titulo = forms.CharField(label = "Titulo",
				max_length = 100,
				placeholder = "Escriba el Titulo")
	descripcion = forms.CharField(label = "Descripcion",
				max_length = 4000,
				help_text = "Escriba la entrada")



class NuevoComentarioForm(forms.Form):
	nombre_usuario = forms.CharField(label = "Nombre de Usuario",
				max_length = 30)
	descripcion = forms.CharField(label = "Comentario",
				max_length = 1000)
	puntuacion = forms.IntegerField(label = "Puntuacion")