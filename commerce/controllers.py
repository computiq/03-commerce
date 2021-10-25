from ninja.router import Router
from commerce.models import Address, City, Label, Merchant, Product, Vendor
from django.http import JsonResponse


commerce_controller = Router()

# Instead of returning the related models as an ID, which is the default behaviour, you should return the related model data!
# Content-Type: application/json


def get_fields(model, prefix=""):
    fields_ = []
    for mod in model._meta.get_fields():
        fields_.append(prefix+mod.name)
    return fields_


"""
* return all products, then return the result QuerySet as a dictionary so Django-Ninja can serialize it to JSON.

http request
GET /commerce/products
"""
@commerce_controller.get("/products", tags = ["products"])
def get_products(request):
    products = Product.objects.select_related("vendor", "merchant", "label").values(
        *get_fields(Product), 
        *get_fields(Vendor,"vendor__"), 
        *get_fields(Merchant, "merchant__"),
        *get_fields(Label, "label__") )

    return JsonResponse( {"products" : list(products) } )

"""
* return all addresses, then like in `products` endpoint, return a dictionary.

http request
GET /commerce/addresses
"""
@commerce_controller.get("/addresses", tags = ["addresses"])
def get_adresess(request):
    addresses = Address.objects.select_related("city").values(*get_fields(Address), *get_fields(City, "city__"))

    return JsonResponse( {"addresses": list(addresses) } )
