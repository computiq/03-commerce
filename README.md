from django.contrib import admin

from commerce.models import Product, Order, Item, Address, OrderStatus, ProductImage, City, Category,Vendor,Merchant,Label

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(ProductImage)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Label)
admin.site.register(Merchant)
admin.site.register(Vendor)


from ninja import Router
from django.shortcuts import render

from commerce.models import Address, Product

commerce_controller = Router()
@commerce_controller.get("products")
def addresses(request):
    return(list(Product.objects.values()))

@commerce_controller.get("addresses")
def addresses(request):
    return(list(Address.objects.values()))
    
    
    """
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from commerce.controllers import commerce_controller

api = NinjaAPI()
api.add_router("commerce", commerce_controller)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("commerce/", api.urls),
]
