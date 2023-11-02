
# API Rest Calculator

Este proyecto tiene la finalidad de subir ficheros en el Bucket de S3 de Amazon Web Services.







![Logo](https://raw.githubusercontent.com/jrojas-t/api_rest_calculator/master/arquitectura.JPG)

**Índice**
- [Pre-requisito](#Pre-requisitos)
- [Montaje de Entorno](#Montaje-de-Entorno)
- [Subir al EC2 de AWS](#Subir-al-ec2-de-aws)


## Pre-requisitos

 - [Python](https://www.python.org/downloads/)
 - [Django](https://www.djangoproject.com/download/)
 - [Postman](https://www.postman.com/downloads/)
 - [MobaXTerm](https://mobaxterm.mobatek.net/download.html)



## Montaje de Entorno

Clonar proyecto

```bash
git clone https://github.com/jrojas-t/api_rest_calculator.git
```

Directorio del proyecto

```bash
cd api_rest_calculator
```

Instalar dependencias

```bash
pip install djangorestframework
pip install psycopg2
pip install boto3
pip install markdown
pip install django-filter
```

Iniciar el servidor

```bash
python manage.py runserver
```

## Subir al EC2 de AWS

La subida del proyecto al EC2 de AWS se debe realizar desde la maquina de Bastion, solo es copiar el fichero.

Copiar el fichero del proyecto al EC2
```bash
scp -r -i /home/ec2-user/ppk/keypair-ree-dev.ppm /home/ec2-user/api_rest_calculator/ ec2-user@10.192.20.121:/home/ec2-user
```
Acceder al EC2 por terminal
```bash
sudo su -
ssh -i /home/ec2-user/ppk/keypair-ree-dev.ppm ec2-user@10.192.20.121
```

Para iniciar el proyecto en EC2, tenemos que acceder al directorio del proyecto
```bash
#Acceder al directorio raiz del proyecto
cd /api_rest_calculator
#Desplegar el proyecto en EC2
python3 manage.py runserver
```