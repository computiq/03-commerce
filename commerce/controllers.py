from ninja import Router

from commerce.models import Address, Product

commerce_controller = Router()

@commerce_controller.get("products")
def addresses(request):
    return(list(Product.objects.values()))

@commerce_controller.get("addresses")
def addresses(request):
    return(list(Address.objects.values()))