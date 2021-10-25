from ninja import Router
from commerce.Schema import prudctsOut
from commerce.Schema import AddressOut
from datetime import date
from typing import List
from ninja import NinjaAPI, Schema

from commerce.models import Address, Product


commerce_control=Router()



#@commerce_control.get('products')
#def list_products(request):
 #   return list(Product.objects.values())


#@commerce_control.get('Address')
#def list_Address(request):
    #return list(Address.objects.values())   
#####
# task    
################################
#**Bonus task:**


@commerce_control.get('pruduct_all',response=List[prudctsOut])
def list_products(request):
    return Product.objects.all() 


@commerce_control.get('all_Address',response=List[AddressOut])
def list_Address(request):
    return Address.objects.all()  
