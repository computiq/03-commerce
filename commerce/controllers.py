from typing import Generator
from ninja import Router
from commerce.models import *

controller_commerce=Router()

@controller_commerce.get("/products")
def gitProducts(request):
    vendor= [i.name for i in list(Vendor.objects.all())]
    merchant= [i.name for i in list(Merchant.objects.all())]
    category= [i.name for i in list(Category.objects.all())]
    label= [i.name for i in list(Label.objects.all())]
    product_item= Product.objects.all()
    product_list = []
    for product in product_item:
     product_list.append({'name' : product.name, 'description' : product.description,
      "weight" : product.weight, "width" : product.width , "height" : product.height ,
      "length" : product.length , 
       "qty" : product.qty , "cost" : product.cost , "price" : product.price ,
      "discounted_price" : product.discounted_price ,
      "vendor" :vendor , "category" : category,"merchant" : merchant , 
       "label" :  label})
    return product_list
   
@controller_commerce.get("/address")   
def gitProducts(request):
    address_item = Address.objects.all()
  
    address_list = []
    for address in address_item:     
     city =  [i.name for i in list(City.objects.all())]
     id=address.id
    
     address_list.append({'address1' : address.address1, 'address2' : address.address2 , 'phone' : address.phone , 'city' : city })
    return address_list    
    