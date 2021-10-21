from ninja import Schema


class CityOut(Schema):
    id: int
    name: str


class AddressOut(Schema):
    id: int
    work_address: bool = None
    address1: str
    address2: str = None
    city: CityOut
    phone: str

class VendorOut(Schema):
    id: int
    name: str
    image: str

class CategoryOut(Schema):
    id: int
    name: str
    description: str
    image: str
    is_active: bool

class MerchantOut(Schema):
    id: int
    name: str

class LabelOut(Schema):
    id: int
    name: str

class ProductOut(Schema):
    id: int
    name: str
    description: str
    weight: float = None
    width: float = None
    height: float = None
    length: float = None
    qty: float
    cost: float
    price: float
    discounted_price: float
    vendor: VendorOut = None
    category: CategoryOut = None
    merchant: MerchantOut = None
    is_featured: bool
    is_active: bool
    label: LabelOut



