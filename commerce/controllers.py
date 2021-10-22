from django.shortcuts import render
from ninja import Router
from typing import List
from ninja import Schema
from commerce.Schemas import productOut , addressOut
from commerce.models import Product, Address
from django.core import serializers

# Create your views here.



commerce = Router()


# Using the list Function  -----------------------------

# @commerce.get('Addresses')
# def addresses(request):
#     return list(Address.objects.all().values())

# @commerce.get('Products')
# def products(request):
#     return list(Product.objects.all().values())


# Using the Schema  ----------------------------------

@commerce.get("Addresses", response=List[addressOut])
def addresses(request):
    return Address.objects.all()
    
@commerce.get("Products", response=List[productOut])
def products(request):
    return Product.objects.all()

# Using the serialization ----------------------------------

@commerce.get("Product")
def serialization_products(request):
    data = serializers.serialize("json", Product.objects.all())
    return data

    