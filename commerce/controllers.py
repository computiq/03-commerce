from django.http import response
from ninja.router import Router
from ninja import Router, Schema
from commerce.models import Product, Address
from django.http import JsonResponse

commerce_controller = Router()


# data = serializers.serialize('json', self.get_queryset())
# return HttpResponse(data, content_type="application/json")

@commerce_controller.get('/products')
def listProducts(request):
    products_qs = Product.objects.select_related('merchant' , 'vendor' ,'category').values()
    return JsonResponse({"Products": list(products_qs)})

@commerce_controller.get('/address')
def listAddress(request):
    address_qs = Address.objects.select_related('city' , 'user').values()
    return JsonResponse({"Address": list(address_qs)})
   
   
