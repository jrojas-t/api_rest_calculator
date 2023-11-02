import json
import logging
import boto3
from botocore.exceptions import ClientError
import os

session = boto3.Session(profile_name='aesydes')
s3_client = session.client('s3')
s3 = session.resource('s3')

def upload_file(jsonObject):

     # Serializando json
    json_object = json.dumps(jsonObject, indent=4)

    # Parametros
    FILE_NAME = 'tmp/file.json'
    BUCKET_NAME = 'aesy-ree-binary-dev'
    KEY_FILE_NAME = 'calculator/{}'.format('file.json')
    response = None

    try:

        if exists_file_in_bucket(BUCKET_NAME, KEY_FILE_NAME) == True:

            #Integración con Bucket S3
            response = s3_client.get_object(Bucket = BUCKET_NAME, Key = KEY_FILE_NAME)
            #Obtenemos el contenido del fichero
            load_json = response['Body'].read().decode('utf-8')
            #Cargamos el contenido en formato JSON
            load_json = json.loads(load_json)
            #Cargamos el contenido en formato JSON con el Body Actual
            new_json = json.loads(json_object)
            #Realizamos el merge del contenido actual y nuevo
            merge_json = load_json.__add__(new_json)
            #Subimos el fichero al Bucket S3
            upload_file_bucket(FILE_NAME, BUCKET_NAME, KEY_FILE_NAME, str(merge_json).replace("'", '"'))

        else:
            #Subimos el fichero al Bucket S3
            upload_file_bucket(FILE_NAME, BUCKET_NAME, KEY_FILE_NAME, json_object)

    except ClientError as e:
        print('Error Code: {}, Message: {}'.format(e.response['Error']['Code'], e.response['Error']['Message']))

#Metodo para verificar si existe el fichero en el Bucket S3
def exists_file_in_bucket(bucket, object_name):

    try:

        my_bucket = s3.Bucket(bucket)

        for object in my_bucket.objects.filter(Prefix=object_name):
            if object.key == object_name:
               return True

    except ClientError as e:
        print('Error Code: {} , Message: {}'.format(e.response['Error']['Code'], e.response['Error']['Message']))

    return False

#Metodo para abrir y escribir en el fichero
def upload_file_bucket(file_name, bucket, key_file_name, json_object):
    try:

        # Abrimos el fichero
        with open(file_name, 'w', encoding='utf8') as outfile:
            #Escribimos en el fichero
            outfile.write(json_object)
        # Subimos el fichero en el Bucket s3
        s3_client.upload_file(file_name, bucket, key_file_name)
    except ClientError as e:
        print('Error Code: {} , Message: {}'.format(e.response['Error']['Code'], e.response['Error']['Message']))
        return False
    return True