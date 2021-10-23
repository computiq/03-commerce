from ninja import Router
from commerce.models import Product,Address
from querybuilder.query import Query


commerce_controller=Router()

@commerce_controller.get("/products")
def get_the_Products(request):
   data =list(Query().from_table(Product).select())
   
   return data

@commerce_controller.get("/Address")
def get_the_Products(request):
   data =list(Query().from_table(Address).select())
   return data