from django.shortcuts import render
from ninja import Router
from .models import Product, Address
from django.http import JsonResponse

test_api = Router(tags=['API Test values'])
product_controller = Router(tags=['Product'])
address_controller = Router(tags=['Address'])


@product_controller.get('')
def list_products(request):

    queryset = Product.objects.all().values()
    return JsonResponse({"Product": list(queryset)})


@address_controller.get('')
def list_address(request):
    data = Address.objects.all().values()
    return JsonResponse({"Address": list(data)})
