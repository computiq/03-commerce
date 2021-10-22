from ninja import Router

from commerce.models import Address, Product

product_controller = Router(tags=['Products'])
address_controller = Router(tags=['Addresses'])

@product_controller.get('product')
def get_products(request):
    return list(Product.objects.values())

@address_controller.get('address')
def get_addresses(request):
    return list(Address.objects.values())
