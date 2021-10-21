from typing import List
from ninja import Router
from .models import Product,Address
from .schemas import AddressOut, ProductOut


commerce_controller = Router(tags=['E-commerce'])

# return all products and return the result QuerySet as a dictionary
@commerce_controller.get('/products')
def get_all_products(request):
    products = Product.objects.all()
    if products :
        products_list_dict = list(products.values())
    else: 
        return {"message":"There is no products to display"}

    return products_list_dict

# return all addresses and return the result QuerySet as a dictionary
@commerce_controller.get('/address')
def get_all_addresses(request):
    address  = Address.objects.all()
    if address: 
        addresses_list_dict = list(address.values())   
    else: 
        return {"message":"There is no Adress to display"}

    return  addresses_list_dict

#---------------------------------------------------------------------------------------------------

# **Bonus task:** (1) for products using schema
@commerce_controller.get("/products/newdisplay", response=List[ProductOut])
def get_products_with_schema(request):
    try :
        products = Product.objects.all()
    except :
        return {"message":"There is no products to display"}
    return products


# **Bonus task:** (2) for adresses using schema
@commerce_controller.get("/addresses/newdisplay", response=List[AddressOut])
def get_addresses_with_schema(request):
    try :
        adresses = Address.objects.all()
    except :
        return {"message":"There is no Adress to display"}

    return adresses