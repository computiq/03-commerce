from django.shortcuts import render

from ninja import Router
from commerce.models import Product
from commerce.models import Address
from commerce.models import Category
from django.http import HttpResponse, response

commerce_controller = Router()
from django.core import serializers


@commerce_controller.get('get_products')
def get_products(request):
    
    k=list(Product.objects.values())

    for index in range(len(k)):
        for key in k[index]:
            if key=='category_id':
                c_id=k[index][key]
                cat= list(Category.objects.values())
    for index in range(len(cat)):
        for key in cat[index]:
            if key=='id':
                if cat[index][key]==c_id:
                    categ=cat[index]   #fetchin  the category
    k.append(categ)
    return k
@commerce_controller.get('get_address')
def get_address(request):
    return list(Address.objects.values())

@commerce_controller.get('get_merchant')
def get_merchant(request):
    print(Address.objects.values())

    return list(Address.objects.values())
