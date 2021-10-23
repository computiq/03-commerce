from ninja import Router,Schema
from commerce.models import Product,Merchant,Vendor,Category,Label,Address
from django.core import serializers
from querybuilder.query import Query


commerce_controller=Router()
class the_data(Schema):
   primary:list
   secondary:list


@commerce_controller.get("/products")
def get_the_Products(request):
   data =list(Query().from_table(Product).select())
   
   return data

@commerce_controller.get("/Address")
def get_the_Products(request):
   data =list(Query().from_table(Address).select())
   return data