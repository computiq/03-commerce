from ninja import Router, Schema
from commerce.models import Product, Address
from typing import List

commerce_controller = Router()


@commerce_controller.get('')
def get_queryset(request):
    return list(Product.objects.values())


@commerce_controller.get('')
def get_address(request):
    return list(Address.objects.values())


class UserSchema(Schema):
    id: int
    first_name: str
    description : str
    weight : float
    width : float
    height : float
    length : float
    qty : int
    cost : int
    price : int
    discounted_price : int
class ProductSchema(Schema):
    id: int
    name: str
    description : str
    weight: float
    width: float
    height: float
    length: float
    qty: int
    cost: int
    price: int
    discounted_price: int
    merchant: UserSchema = None


@commerce_controller.get("/Product", response=List[ProductSchema])
def tasks(request):
    queryset = Product.objects.all()
    return list(queryset)
