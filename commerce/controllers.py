from ninja import Router, ModelSchema
from commerce.models import Product, Address, User, City
from ninja.orm import create_schema
from typing import List

commerce_controller = Router()

UserSchema = create_schema(User, exclude= ['password', 'last_login', 'user_permissions','is_superuser','groups','is_staff','is_active'])
CitySchema = create_schema(City)

class AddressSchema(ModelSchema):
    class Config:
        model =Address
        model_fields = ['id', 'user', 'address1', 'address2', 'work_address', 'city', 'phone']
    user: UserSchema
    city: CitySchema

@commerce_controller.get("products")
def show_products(request):
    return list(Product.objects.values())

@commerce_controller.get("addresses", response=List[AddressSchema])
def show_addresses(request):
    return list(Address.objects.select_related("city","user").all())