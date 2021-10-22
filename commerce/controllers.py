from django.shortcuts import render

from ninja import Router
from commerce.models import Product
from commerce.models import Address

commerce_controller = Router()
from django.core import serializers


@commerce_controller.get('get_products')
def get_products(request):
    return list(Product.objects.values())


@commerce_controller.get('get_address')
def get_address(request):
    return list(Address.objects.values())

