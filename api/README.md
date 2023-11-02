
# Módulo API (api)

En este módulo encontraremos la organización de paquetes de utilidad y servicios que se encontrarán integrados con la aplicación del proyecto.

**Índice**
- [Paquetes](#Paquetes)
- [Ficheros de Configuración](#Ficheros-de-configuracion)

## Paquetes

Los paquetes que se han creado para este proyecto son:

- ./api/services

En este paquete se deben de crear las clases que contienen la lógica del negocio.

- ./api/utils

En este paquete se debe crear las clases que nos serviran de utilidad en el proyecto de forma generica (ejemplo: clases que contengan validaciones de sintaxis, métodos y validaciones genéricas, etc).


## Ficheros de Configuración
Al ejecutar el comando anterior se creará los siguientes módulos

### api/ ###
- ./api/serializers.py: Se configura las entidades que seran utilizadas en el proyecto para ser serializarlas.

- ./api/urls.py: Se configuran los endpoints de la aplicación.

- ./api/view.py: Es la capa vista del API Rest, se definirá los servicios a ser publicados.