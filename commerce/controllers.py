from django.shortcuts import render
from ninja import Router
from commerce.models import *

# Create your views here.
product_control = Router()
address_control = Router()


@product_control.get('')
def list_products(request):
    return list(Product.object.all().values())


@address_control.get('')
def list_addresses(request):
    return list(Product.object.all().values())
