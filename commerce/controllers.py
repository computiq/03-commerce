from django.shortcuts import render
from ninja import Router
from commerce.models import Product, Address, Vendor, Category, Merchant, Label, User, City

products = Router()
addresses = Router()

@products.get("/products")
def get_products(request):
    product_list = list(Product.objects.values())

    for product in product_list:
        category_id = product['category_id']
        del product['category_id']
        product['category'] = list(Category.objects.filter(id=category_id).values())[0]

        label_id = product['label_id']
        del product['label_id']
        product['label'] = list(Label.objects.filter(id=label_id).values())[0]

        merchant_id = product['merchant_id']
        del product['merchant_id']
        product['merchant'] = list(Merchant.objects.filter(id=merchant_id).values())[0]

        vendor_id = product['vendor_id']
        del product['vendor_id']
        product['vendor'] = list(Vendor.objects.filter(id=vendor_id).values())[0]

    return product_list

@addresses.get("/addresses")
def get_addresses(request):
    addresses = list(Address.objects.values())
    for address in addresses:
        user_id = address['user_id']
        del address['user_id']
        address['user'] = list(User.objects.filter(id=user_id).values())[0]
        
        city_id = address['city_id']
        del address['city_id']
        address['city'] = list(City.objects.filter(id=city_id).values())[0]

    return addresses