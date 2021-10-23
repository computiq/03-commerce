from django.shortcuts import render
from django.http import request
from ninja import Router,Schema
from commerce.models import Product, Address, City
from django.core import serializers

commerce_conttroller=Router()
# Create your views here.


@commerce_conttroller.get('ptoducts')
def products_list(request):
    return list(Product.objects.values())

@commerce_conttroller.get('adresses')
def adresses_list(request):
    return list(Address.objects.values())
# @commerce_conttroller.get('city')
# def city_fromadd_list(request):
#     cities=serializers.serialize("json",list(Address.objects.select_related("city")))
    
#     return cities