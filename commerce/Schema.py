
from ninja import Schema
from datetime import date



class vendorOut(Schema):
    id:int
    name:str
    image:str



class categoryOut(Schema):
    id:int
    name:str
    description:str
    is_active:bool


class merchantOut(Schema):
    id: int
    name: str



class labeliOut(Schema):
    id: int
    name: str
class prudctsOut(Schema):
    id: int
    name: str
    description:str
    weight: float=None
    width : float=None
    height: float=None
    length: float=None
    qty: float
    cost: float
    price: float
    discounted_price: float
    vendor :vendorOut=None
    category: categoryOut=None
    merchant: merchantOut=None
    is_featured: bool
    is_active: bool
    label: labeliOut=None


class cityOut(Schema):
    id: int
    name: str

class AddressOut(Schema):
    id: int
    work_address: bool=None
    address1: str
    address2: str=None
    city: cityOut
    phone: str    




