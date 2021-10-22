from django.shortcuts import render
from ninja import Router

products_controller = Router(tags = ['products'])
adresses_controller = Router(tags = ['adresses'])

@products_controller.get('/products')
def listProducts(request):
    return list(Product.objects.all())

@adresses_controller.get('/adresses')
def listAdresses(request):
   return list(Address.objects.all())
#incase someone is stalking my solution, I'm not finished c;
