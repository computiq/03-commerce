from django.http import HttpResponse
from ninja import Router
from commerce.models import Product, Address
from django.core import serializers
from django.forms.models import model_to_dict

productsController = Router()
addressesController = Router()
bonusTaskController = Router()


@productsController.get('')
def get_all_products(request):
    queryset = Product.objects.all()
    addresses = serializers.serialize("json", queryset)
    return HttpResponse(addresses, content_type="application/json")


@addressesController.get('')
def get_all_addresses(request):
    queryset = Address.objects.all()
    addresses = serializers.serialize("json", queryset)
    return HttpResponse(addresses, content_type="application/json")

@bonusTaskController.get('')
def get_products_details(request):
    products_query = Product.objects.select_related('merchant', 'category', 'vendor', 'label')

    # the below solution done using natural_key method that will be used to resolve foreignkey when
    # serializers.serialize() invoked. this will return all data of related models including the inherited from
    # Entity model
    data = serializers.serialize('json', products_query, use_natural_foreign_keys=True)
    return HttpResponse(data, content_type="application/json")

    # while this will return just the related models data without the inherited from base model
    # products = [{key: getattr(product, key) for key in model_to_dict(product).keys()} for product in products_query]
    # for product in products:
    #     for k, v in product.items():
    #         if hasattr(product[k], '__dict__'):
    #             product[k] = model_to_dict(product[k])
    #
    # return products
