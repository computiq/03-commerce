from django.db import router
from django.http.response import JsonResponse
from django.shortcuts import render
from ninja.router import Router
from commerce.models import Address, Product
from ninja import NinjaAPI
from django.forms.models import model_to_dict
from django.http import JsonResponse




# Create your views here.
api= NinjaAPI()

product_c= Router()
address_c = Router()

@product_c.get('/')
def all_product(request):
    #return JsonResponse({"product", list(Product.objects.all())}) 
    data= Product.objects.all().values()
    return JsonResponse({"product": list(data)}) 

@address_c.get('/address')
def all_add(request):
    ddata= Address.objects.all().values()
    return JsonResponse({"address": list(ddata)}) 

