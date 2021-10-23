from ninja import Router

from commerce.models import *

commerce_controller = Router()


@commerce_controller.get("products")
def show_products(request):
    response = []
    for item in Product.objects.values():
        label_id = item.pop("label_id")
        vendor_id = item.pop("vendor_id")
        category_id = item.pop("category_id")
        merchant_id = item.pop("merchant_id")
        item["label"] = list(Label.objects.all().filter(id=label_id).values())[0]
        item["vendor"] = list(Vendor.objects.all().filter(id=vendor_id).values())[0]
        item["category"] = list(Category.objects.all().filter(id=category_id).values())[0]
        item["merchant"] = list(Merchant.objects.all().filter(id=merchant_id).values())[0]
        response.append(item)
    return response


@commerce_controller.get("addresses")
def show_addresses(request):
    response = []
    for item in Address.objects.values():
        city_id = item.pop("city_id")
        item["city"] = list(City.objects.all().filter(id=city_id).values())[0]
        response.append(item)
    return response


