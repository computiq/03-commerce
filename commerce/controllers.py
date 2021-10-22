from ninja import Router
from commerce.models import Product,Merchant,Vendor,Category,Label,Address
from django.core import serializers

commerce_controller=Router()

@commerce_controller.get("/products")
def get_the_Products(request):
   data = serializers.serialize("json", Product.objects.all())
  
   return data

@commerce_controller.get("/Address")
def get_the_Products(request):
   data = serializers.serialize("json", Address.objects.all())
   return data