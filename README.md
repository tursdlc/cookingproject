# Savor Street - Web de Recetas - Backend

1. ## Descripción
   
Este es el repositorio del backend para proporcionar una API REST que permite al usuario crear, editar, ver y eliminar recetas de cocina en la parte frontend con React (https://github.com/tursdlc/frontCookingRecipes); está construida con **Django** y **Django REST Framework**. 

2. ## Funcionalidades

- **API REST**: El backend ofrece una API completa para la gestión de recetas (CRUD: Crear, Leer, Actualizar, Eliminar).
- **Gestión de Base de Datos**: Se utiliza **PostgreSQL** para almacenar la información de las recetas.

3. ## Tecnologías Utilizadas

- **Django**: Framework web para el backend.
- **Django REST Framework (DRF)**: Para crear los endpoints de la API.
- **PostgreSQL**: Base de datos para almacenar los datos de las recetas.
- **CORS Headers**: Para permitir que el frontend de React se comunique con el backend.

4. ## Instalación y Configuración

### Prerrequisitos

- Python 3.8+
- Django
- Django REST Framework
- CORS Headers
- Virtualenv

### Pasos para la instalación

1. Clona el repositorio del backend:
   ```bash
   git clone https://github.com/tuusuario/tu-repo-backend.git
   cd tu-repo-backend
   
2. Crea y activa un entorno virtual:
   python -m venv env
   .\env\Scripts\activate
   
3. Instala las dependencias:
   pip install -r requirements.txt

4. Configura las variables de entorno en un archivo .env en la carpeta raíz del proyecto:
   SECRET_KEY=tu_clave_secreta
   DEBUG=True
   ALLOWED_HOSTS=localhost

5. Aplica las migraciones para configurar la base de datos:
   python manage.py migrate

6. Para crear un superusuario para el panel de administración de Django:
   python manage.py createsuperuser

7. Ejecuta el servidor de desarrollo:
   python manage.py runserver


##Configuración de CORS

Para permitir que el frontend acceda a la API, debes configurar el middleware de CORS en settings.py:

# settings.py
INSTALLED_APPS = [
 'corsheaders',
    'rest_framework',
    
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    
]

# Permitir solicitudes del frontend de React
CORS_ALLOW_ALL_ORIGINS = True  # Para desarrollo



   
   
   
