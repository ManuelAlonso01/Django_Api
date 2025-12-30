# 🎬 Movie & Series API (Django REST)

API REST desarrollada con Django y Django Rest Framework para gestionar un catálogo de películas y series, con soporte de autenticación y control de permisos para operaciones sensibles.

## 🚀 Funcionalidades

- CRUD completo de películas y series.

- Listado y detalle por ID.
- Búsqueda por título.

- Filtrado por género.
- Autenticación por token.

- Permisos: solo usuarios  administradores pueden crear, editar o eliminar contenido.

## 🧱 Stack tecnológico

- Python

- Django

- Django REST Framework

- PostgreSQL

## 🛠️ Instalación

- Clonar el repositorio.

- Crear un entorno virtual:
   ```bash
   python -m venv venv
   ```


- Activar el entorno:
   ```bash
   # Windows
   .\venv\Scripts\activate

   # Linux / Mac
   source venv/bin/activate
   ```


- Instalar dependencias:

   ```bash
   pip install django djangorestframework psycopg2-binary
   ```


- Ejecutar migraciones:

   ```bash
   python manage.py migrate
   ```


- Crear un superusuario:
   ```bash
   python manage.py createsuperuser
   ```


- Crear un token de autenticación:

   ```bash 
   python manage.py shell
   ```
   ```python
   from django.contrib.auth.models import User
   from rest_framework.authtoken.models import Token

   user = User.objects.get(username="admin")
   token, created = Token.objects.get_or_create(user=user)
   print(token.key)
   ```



- Ejecutar el servidor:
   ```bash
   python manage.py runserver
   ```

## 🔐 Autenticación

- Los endpoints protegidos requieren enviar el token en el header HTTP:
- Authorization: Token <tu_token>

## 📌 Endpoints
- 🔍 GET

   - GET /movies/ → Lista todas las películas.

   - GET /series/ → Lista todas las series.

   - GET /movies/id/<<int:id>>/ → Detalle de una película.

   - GET /series/id/<<int:id>>/ → Detalle de una serie.

   - GET /movies/genre/<<str:genre>>/ → Películas por género.

   - GET /series/genre/<<str:genre>>/ → Series por género.

   - GET /movies/title/<<str:title>>/ → Buscar película por título.

   - GET /series/title/<<str:title>>/ → Buscar serie por título.

- ✍️ POST (solo admin)

   - POST /movies/create/ → Crear una película.

   - POST /series/create/ → Crear una serie.

- ♻️ PATCH (solo admin)

   - PATCH /movies/update/<<int:id>>/ → Actualizar película.

   - PATCH /series/update/<<int:id>>/ → Actualizar serie.

- 🗑️ DELETE (solo admin)

   - DELETE /movies/delete/<<int:id>>/ → Eliminar película.

   - DELETE /series/delete/<<int:id>>/ → Eliminar serie.

## ✒️ Autor

- Manuel Alonso
- 👉 https://github.com/ManuelAlonso01
