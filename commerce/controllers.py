from typing import List
from ninja import Router 
from ninja.orm import create_schema
from commerce.models import Product, Address 



all_products = create_schema(Product, depth= 2)
all_address = create_schema(Address, depth= 1)


commerce = Router()

@commerce.get('productsall' , response= List[all_products])
def getall_product(request):
    return Product.objects.all()

@commerce.get('addressall' , response= List[all_address])
def getall_address(request):
    return Address.objects.all()
    