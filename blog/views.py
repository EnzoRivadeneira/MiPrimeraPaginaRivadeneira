from django.shortcuts import render, redirect
from .forms import AutorForm, GeneroForm, LibroForm

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_autor')
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})

def crear_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_genero')
    else:
        form = GeneroForm()
    return render(request, 'blog/crear_genero.html', {'form': form})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_libro')
    else:
        form = LibroForm()
    return render(request, 'blog/crear_libro.html', {'form': form})

def buscar_libro(request):
    resultado = []
    if request.method == 'POST':
        form = BuscarLibroForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultado = Libro.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarLibroForm()
    
    return render(request, 'blog/buscar_libro.html', {'form': form, 'resultado': resultado})
