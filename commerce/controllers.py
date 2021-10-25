from django.shortcuts import render
from .models import Product,Address
from ninja import Router
from django.db import models

# Create your views here.


objects = models.Manager()

product_controller = Router()
address_controller = Router()


@product_controller.get('')
def list_products(request):
    return list(Product.objects.values())


@address_controller.get('')
def list_addresses(request):
    return list(Address.objects.values())
