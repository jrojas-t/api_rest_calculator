
# Módulo de Configuración de Base de Datos (base)

En este módulo contendra todos los ficheros de integración con la base de datos PostgreSQL soportadas por DJango.

**Índice**
- [Base de Datos](#Base-de-datos)
- [Configuración de Conexión PostgreSQL](#Configuracion-de-conexion-postgresql)
- [Ficheros de Configuración](#Ficheros-de-configuracion)


## Base de datos

 - [PostgreSQL](https://docs.djangoproject.com/en/4.2/ref/databases/#postgresql-notes)
 - [MariaDB](https://docs.djangoproject.com/en/4.2/ref/databases/#mariadb-notes)
 - [MySQL](https://docs.djangoproject.com/en/4.2/ref/databases/#mysql-notes)
 - [Oracle](https://docs.djangoproject.com/en/4.2/ref/databases/#oracle-notes)
 - [SQLite](https://docs.djangoproject.com/en/4.2/ref/databases/#sqlite-notes)

También hay una serie de librerías de base de datos proporcionadas por terceros


## Configuración de Conexión PostgreSQL

settings.py

En este fichero se realiza la configuración de los parametros de la base de datos.

```bash
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'NAME_DATABASE',
        'USER': 'USER_DATABASE',
        'PASSWORD': '******',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
```

Creación del módulo base

```bash
python manage.py startapp base
```

Instalar dependencias

```bash
pip install psycopg2
pip install shell
```

Iniciar el servidor

```bash
python manage.py runserver
```

## Ficheros de Configuración
Al ejecutar el comando anterior se creará los siguientes módulos

### base/ ###
- models.py: Se debe definir la(s) entidad(es) con sus parámetros.

