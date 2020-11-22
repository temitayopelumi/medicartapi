from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Product, Account
from .serializers import ProductSerializer, RegistrationSerializer, AccountPropertiesSerializer


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def api_product(request, pk):
    product = Product.objects.get(id=pk)
    serializers = ProductSerializer(product, many=False)
    return Response(serializers.data)


@api_view(['GET'])
def Productlist(request):
    product = Product.objects.all()
    serializers = ProductSerializer(product, many=True)
    return Response(serializers.data)

# @api_view(['POST'])
# def taskCreate(request):
#     serializers = TaskSerializers(data=request.data)
#     if serializers.is_valid():
#         serializers.save()
#     return Response(serializers.data)

#

@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser))
def addProduct(request):
    serializers = ProductSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def UpdateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializers = ProductSerializer(instance=product, data=request.data)
    if serializers.is_valid():
        serializers.save()
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

from rest_framework import filters

class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category']

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def account_properties_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountPropertiesSerializer(account)
        return Response(serializer.data)

@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def update_account_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AccountPropertiesSerializer(account, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Account update success'
        return Response(data=data)
    return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

