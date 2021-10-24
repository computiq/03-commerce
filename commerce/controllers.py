from ninja.orm import create_schema
from ninja import Router, ModelSchema
from commerce.models import Product,Address,User,City,Vendor,Category,Merchant,Label
from typing import List


create_user = create_schema(User,  exclude= 
['password', 'last_login', 'user_permissions','is_superuser','groups','is_staff','is_active'])

citySchema = create_schema(City)

create_Product = create_schema(Product, depth=1)


c_router=Router() 


class AddressSchema(ModelSchema):
    class Config:
        model =Address
        model_fields = [ 'user', 'address1', 'city', 'phone']
    user: create_user
    city: citySchema



class productSchema(ModelSchema):
    class Config:
        model =Product
        model_fields = [ "category", "vendor", "merchant", "label"]
    
    


@c_router.get('product/')
def get_product(request):
    return list(Product.objects.all().values())



@c_router.get('addrss/')
def get_address(request):
    return list(Address.objects.all().values())




@c_router.get("address/",response=List[AddressSchema])
def get_addres(request):
   
    return list(Address.objects.select_related("user","city").all())




@c_router.get("product2/",response=List[productSchema])
def get_addres(request):
   
    return list(Product.objects.select_related("category", "vendor", "merchant", "label").all())