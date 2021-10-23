from ninja import Router
from typing import List
from commerce.models import Product, Address


productsController = Router()
addressesController = Router()



@productsController.get('')
def list_products(request):
    return list(Product.objects.all().values())


@addressesController.get('')
def list_adderess(request):
    return list(Address.objects.all().values())



""""
I am still thinking of a solution bonus task

"""