from commerce.schemas import AddressOut, ProductOut
from ninja import Router
from commerce.models import Address, Product
from typing import List
from typing import List
from ninja import Router



product_controller = Router(tags=['product'])
address_controller = Router(tags=['address'])



# Task 1 & 2
"""Using List Function"""
# @address_controller.get("/all")
# def list_adresses(request):
#     return list(Address.objects.all().values())


# @product_controller.get("/all")
# def list_adresses(request):
#     return list(Product.objects.all().values())


# Bonus task
"""Using Schema""" 
@address_controller.get("/all", response=List[AddressOut])
def list_adresses(request):
    return Address.objects.all()

@product_controller.get("/all", response=List[ProductOut])
def list_products(request):
    return Product.objects.all()





"""Another Method: Django Serializing"""
#from django.core.serializers import serialize
# @address_controller.get("/all")
# def list_adresses(request):
#   retun serialize('json', Address.objects.all())