from django.shortcuts import render
from ninja import Router 
from commerce.models import Product,Address
from typing import List

c_router=Router() 




@c_router.get('prodect/')
def get_prodet(request):
    return list(Product.objects.all().values())


@c_router.get('adderss/')
def get_adderess(request):
    return list(Address.objects.all().values())



'''

'''
