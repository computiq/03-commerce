from django.shortcuts import render

from ninja import Router
from commerce.models import Address, Product
from typing import List
address_controller = Router()
product_controller = Router()


@product_controller.get('')
def list_products(request):
    return list(Product.objects.all().values())


@address_controller.get('')
def list_products(request):
    return list(Address.objects.all().values())
