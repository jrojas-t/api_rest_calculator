from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import connectionElementViewServices
from .utils.upload_file import upload_file

@api_view(['GET'])
def get(request):
    serializer = connectionElementViewServices.getAll(request)
    upload_file(serializer.data)
    return Response(serializer.data)