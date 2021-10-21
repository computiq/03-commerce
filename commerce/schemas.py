from ninja import Schema
from pydantic import EmailStr

from commerce.models import User

class VendrOut(Schema):
    name : str  
    image : str = None

class CategoryOut(Schema):
    name : str  
    description :str  = None
    image :  str = None
    is_active : str = None

class MerchantOut(Schema):
    name : str 

class LabelOut(Schema):
    name : str 

class ProductOut(Schema) : 
    name : str 
    description : str = None
    weight : int = None
    width : int = None
    height : int  = None
    length : int  = None
    qty : float  
    cost : float 
    price : float 
    discounted_price : float 
    vendor : VendrOut = None
    category : CategoryOut =None
    merchant : MerchantOut = None
    is_featured  : str = None
    is_active  : str = None
    label : LabelOut = None



class UserOut(Schema):
    username : str
    email : str = None 

class CityOut(Schema):
    name : str 

class AddressOut(Schema):
    user : UserOut 
    work_address : str = None
    address1 : str 
    address2 : str = None
    city : CityOut
    phone : str 