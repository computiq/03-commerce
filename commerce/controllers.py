from ninja import Router

from commerce.models import Address, Product


commerce_control=Router()


@commerce_control.get('products')
def list_products(request):
    return list(Product.objects.values())


@commerce_control.get('Address')
def list_Address(request):
    return list(Address.objects.values())   
    

