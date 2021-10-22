from django.http import HttpResponse
from ninja import Router
from commerce.models import Product, Address
from django.core import serializers

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

# still working on this
# @bonusTaskController.get('')
# def get_bonus(request):
#     queryset0 = Product.objects.select_related('merchant','category','label')

