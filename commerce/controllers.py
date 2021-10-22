from django.shortcuts import render
from ninja import Router, Schema
from ninja.main import NinjaAPI
from django.http import JsonResponse
from .models import Category, Product , Address



commerce_controllers = Router()

@commerce_controllers.get("products")
def fetch_products(request):
    result= Product.objects.values()
    list_result = [p for p in result] 
    return list_result


@commerce_controllers.get("addresses")
def fetch_address(request):
    result= Address.objects.values()
    list_result = [p for p in result] 
    return list_result











