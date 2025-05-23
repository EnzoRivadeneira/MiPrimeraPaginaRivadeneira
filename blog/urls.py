from django.urls import path
from . import views

urlpatterns = [
    path('autor/', views.crear_autor, name='crear_autor'),
    path('genero/', views.crear_genero, name='crear_genero'),
    path('libro/', views.crear_libro, name='crear_libro'),
]

path('buscar/', views.buscar_libro, name='buscar_libro'),