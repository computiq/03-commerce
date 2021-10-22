from ninja import Schema


class cityOut(Schema):
    id: int
    name: str


class addressOut(Schema):
    id: int
    work_address: bool = None
    address1: str
    address2: str = None
    city: cityOut
    phone: str


class vendorOut(Schema):
    id: int
    name: str
    image: str


class categoryOut(Schema):
    id: int
    name: str
    description: str
    image: str
    is_active: bool


class merchantOut(Schema):
    id: int
    name: str


class labelOut(Schema):
    id: int
    name: str


class productOut(Schema):
    id: int
    name: str
    description: str
    weight: float = None
    width: float = None
    height: float = None
    length: float = None
    qty: int
    cost: int
    price: int
    discounted_price: int
    vendor: vendorOut = None
    category: categoryOut = None
    merchant: merchantOut = None
    is_featured: bool = None
    is_active: bool = None
    label: labelOut = None
