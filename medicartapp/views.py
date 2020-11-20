from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer, RegistrationSerializer

@api_view(['GET', ])
def api_product(request, pk):
    product = Product.objects.get(id=pk)
    serializers = ProductSerializer(product, many=False)
    return Response(serializers.data)

@api_view(['GET'])
def Productlist(request):
    product = Product.objects.all()
    serializers = ProductSerializer(product, many=True)
    return Response(serializers.data)

@api_view(['POST',])
def registration_view(request):

    if  request.method  == 'POST':
        serializer= RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] =  'successfully registered a new user'
            # data['email'] = account.email
            # data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)