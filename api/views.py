from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import *
from .utils.upload_file import *

@api_view(['GET'])
def get(request):
    serializer = connectionElementViewServices.getAll(request)
    upload_file(serializer.data)
    return Response(serializer.data)