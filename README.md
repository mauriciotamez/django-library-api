

# Django Library 📖


Una REST-API basada en una biblioteca, donde los usuarios 
pueden rentar y ver todos los libros disponibles, desarrollada con Django-Rest-Framework.


## Table of Contents


- [Installation](#installation)
- [Usage](#usage)
- [Endpoints y Admin](#endpoints)
- [SwaggerUI y JWT](#swaggerui)





## Installation 
Corre todos los comandos en orden.


```sh
git clone https://github.com/mauriciotamez/django-library-api.git // clone the repo
cd django-library-api // go into the cloned repo dir
python3 -m venv venv // create a virtual enviroment
source venv/bin/activate // activate the virtual env
pip install -r requirements.txt // install all the requirements
```
## Usage
 Crear la base de datos y correr las migraciones. 🚀


Si quieres correr la aplicación en localhost tendrás que crear una base de datos Postgres local llamada
```library-api``` una vez hecha tu base de datos tendrás que correr las migraciones con
el comando ```python3 manage.py migrate```


Puedes verificar que las migraciones se hayan aplicado a tu base de datos por medio
de algún cliente como ```pg-admin``` o ```dbeaver```.


Si todo sale bien deberías poder correr ``` python3 manage.py runserver``` y tus migraciones
deberían estar correctas.


### Endpoints


Puedes ver todos los endpoints disponibles por medio de esta URI ``` http://127.0.0.1:8000/api/schema/swagger-ui/```


Para empezar a interactuar con la base de datos necesitaras un usuario administrador
para eso corre el comando ```python3 manage.py createsuperuser ``` una vez hecho tu 
usuario admin podrás dirigirte a la URL ```http://localhost:8000/admin ``` e ingresar tus credenciales
para revisar que se haya creado correctamente, desde el panel de admin puedes crear, modificar
o borrar datos.


### SwaggerUI
Una vez generado un usuario admin, puedes ingresar tus credenciales en la URL ```http://localhost:8000/api/token/ ```
ese token lo puedes utilizar para cualquier petición por medio de algun cliente como ```postman ``` o ``` insomnia```.


A su vez puedes autorizar y ejecutar métodos en la Swagger UI 
```http://127.0.0.1:8000/api/schema/swagger-ui/ ``` dándole al botón authorize e ingresando
el token obtenido previamente.


