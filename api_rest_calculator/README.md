
# Módulo de Configuración (base)

En este módulo encontraremos los ficheros de configuración que se utilizaran en la ejecución del proyecto.

**Índice**
- [Creación del proyecto](#Creacion-del-proyecto)
- [Ficheros de Configuración](#Ficheros-de-configuracion)

>**Importante**
>
>Este comando se debe ejecutar en la raiz del proyecto
>
>NOTA: Solo se debe utilizar cuando se requiere crear el proyecto (solo una única vez).

## Integración con base de datos

```bash
django-admin startproject api-rest-calculator
```

## Ficheros de Configuración
Al ejecutar el comando anterior se creará los siguientes módulos

### api_rest_calculator/ ###
- asgi.py: Se configura las variables de entornos y sub-modulos de configuración.

- settings.py: Se configura las librerias de terceros, plantillas, configuración de base de datos y parámetros como secrets_keys, urls, time zones, etc.

- urls.py: Se configura la lista de patrones de urls para las vistas.

- wsgi.py: Se configura la aplicación por defecto
