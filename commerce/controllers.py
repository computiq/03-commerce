from django.shortcuts import render
from ninja import Router
from commerce.models import Product, Address


products_controller = Router(tags = ['products'])
addresses_controller = Router(tags = ['addresses'])

@products_controller.get('')
def listProducts(request):
    return list(Product.objects.values())

@addresses_controller.get('')
def listAdresses(request):
   return list(Address.objects.values())

