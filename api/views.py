from rest_framework.response import Response  # used to output data passed to it as json
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def get_data(request):
    # drink_1 = {"name": "Coca-Cola", "size": "50cl", "description": "refreshingly good...."}
    drinks = Item.objects.all()
    serializer = ItemSerializer(drinks, many=True)  # setting it to true tells your serializer that it's serializing
    # multiple items
    return Response(serializer.data)


@api_view(['POST'])
def add_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
