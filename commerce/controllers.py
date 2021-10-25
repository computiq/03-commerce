from rest_framework.response import Response
from ninja import Router
from rest_framework.decorators import api_view, throttle_classes
from commerce.models import Product, Address, Merchant, Vendor, Label, Address, City, Category

commerce_controller = Router()


@commerce_controller.get("/products")
def get_products(request):
    vendor = [i.name for i in list(Vendor.objects.all())]
    merchant = [i.name for i in list(Merchant.objects.all())]
    category = [i.name for i in list(Category.objects.all())]
    label = [i.name for i in list(Label.objects.all())]
    product_item = Product.objects.all()
    products = []
    for product in product_item:
        products.append({'name': product.name, 'description': product.description,
                             "weight": product.weight, "width": product.width, "height": product.height,
                             "length": product.length,
                             "qty": product.qty, "cost": product.cost, "price": product.price,
                             "discounted_price": product.discounted_price,
                             "vendor": vendor, "category": category, "merchant": merchant,
                             "label": label})
    return products


@commerce_controller.get("/address")
def list_address(request):
    address_item = Address.objects.all()

    addresss = []
    for address in address_item:
        city = [i.name for i in list(City.objects.all())]
        id = address.id

        addresss.append(
            {'address1': address.address1, 'address2': address.address2, 'phone': address.phone, 'city': city})
    return addresss

