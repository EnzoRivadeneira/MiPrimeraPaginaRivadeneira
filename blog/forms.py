from django import forms
from .models import Autor, Genero, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'fecha_nacimiento']

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero', 'fecha_publicacion', 'sinopsis']

class BuscarLibroForm(forms.Form):
    titulo = forms.CharField(label='Buscar por título', max_length=100)
