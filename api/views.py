from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework.decorators import api_view
from core.models import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def products_list(request):
    product = Products.objects.all()
    serializer = ProductsSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product(request, pk):
    product = get_object_or_404(Products, id=pk)
    serializer = ProductsSerializer(product)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def product_view(request):
    if request.method == 'GET':
        product = Products.objects.all()
        serializer = ProductsSerializer(product, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

@api_view(['GET', 'PUT', 'DELETE'])
def each_product(request, pk):
    product = get_object_or_404(Products, id=pk)

    # try:
    #     product = Products.objects.get(id=pk)
    # except Products.DoesNotExist:
    #     return Response({"error" : "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductsSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)