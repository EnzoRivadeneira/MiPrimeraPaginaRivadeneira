# MiPrimeraPaginaRivadeneira

Este es un proyecto web desarrollado en Django que simula un blog de libros. Se construyó para el Trabajo Práctico de la materia Programación, aplicando el patrón MVT y los componentes fundamentales de Django: modelos, vistas, formularios, herencia de plantillas, y uso de base de datos.

---

## ¿Qué funcionalidades incluye?

- Herencia de plantillas HTML con un archivo `base.html`.
- Tres modelos: `Autor`, `Género` y `Libro`.
- Un formulario para crear objetos de cada uno de esos modelos.
- Un formulario para **buscar libros** en la base de datos por título.
- Navegación entre páginas usando rutas simples.

---

## ¿Cómo probar el proyecto?

## 1. Clonar el repositorio

```bash
git clone https://github.com/EnzoRivadeneira/TuPrimeraPaginaRivadeneira.git
cd TuPrimeraPaginaRivadeneira



## 2. Crear el entorno virtual
bash

python -m venv venv


## 3. Activar el entorno virtual
En Windows (CMD):

bash

venv\Scripts\activate



## 4. Instalar dependencias (Django)
bash

pip install django


## 5. Aplicar las migraciones a la base de datos
bash

python manage.py makemigrations
python manage.py migrate

## 6. Iniciar el servidor
bash

python manage.py runserver


## 7. Usar la aplicación
Abrí el navegador en http://127.0.0.1:8000/ y accedé a las siguientes rutas:

/autor/ → Crear un autor.

/genero/ → Crear un género.

/libro/ → Crear un libro (requiere autor y género previamente creados).

/buscar/ → Buscar libros por título (completo o parcial).



## Orden de prueba sugerido
Crear primero al menos un autor.

Crear al menos un género.

Crear uno o más libros eligiendo autor y género.

Probar la búsqueda de libros en /buscar/.





## Estructura general del proyecto
csharp

MiPrimeraPaginaRivadeneira/
├── blog/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── blog/
│           ├── crear_autor.html
│           ├── crear_genero.html
│           ├── crear_libro.html
│           ├── buscar_libro.html
│       └── base.html
├── manage.py
├── MiPrimeraPaginaRivadeneira/
│   └── settings.py
├── venv/
└── README.md



