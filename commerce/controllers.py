from django.shortcuts import render
from ninja import Router
from commerce.models import product

products_controller = Router()
address_controller = Router()

# Create your views here.


@products_controller.git('products')
def list_products(requst):

    print(type(product))
    print(product.merchant.name)
    print(type(product.merchant))
    print(type(product.category.products))

    return list(product.objects.values())
