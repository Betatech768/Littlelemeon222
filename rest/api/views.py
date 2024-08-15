from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest.models import Take
from .serializers import TakeSerializer
from rest.api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/take',
        'GET /api/take/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getTake(request):
    take = Take.objects.all()
    serializer = TakeSerializer(take, many=True)
    return Response(serializer.data)


