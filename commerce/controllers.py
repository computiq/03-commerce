from django.shortcuts import render
from ninja import Router
from django.http import JsonResponse
from commerce.models import Product, Address


commerce_controller = Router()


@commerce_controller.get('/api/products')
def list_products(request):
    result = list( Product.objects.values())

    return JsonResponse(result, safe=False)



@commerce_controller.get('/api/addresses')
def list_addresses(request):
    result = list( Address.objects.values())

    return JsonResponse(result, safe=False)



