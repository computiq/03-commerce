import json
from django.shortcuts import render
from ninja import Router
from django.http import JsonResponse
from rest_framework import serializers

from django.contrib.auth.models import User

from commerce.models import City
from commerce.models import Product
from commerce.models import Address
from .serializers import AddressSerializer


commerce_controller = Router()


@commerce_controller.get('/api/products')
def list_products(request):
    result =list( Product.objects.values())

    return JsonResponse(result, safe=False)



@commerce_controller.get('/api/addresses')
def list_addresses(request):
    result = list( Address.objects.values())

    return JsonResponse(result, safe=False)



