
from rest_framework.response import Response
from ninja import Router
from rest_framework.decorators import api_view, throttle_classes
from commerce.models import Product, Address


commerce_controller = Router()


@commerce_controller.get('/address', )
def list_address(request):
    address = Address.objects.all()

    return  list(Address.objects.values())

@commerce_controller.get('/products')
def get_products(request):
    return list(Product.objects.values())
