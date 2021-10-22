from ninja import Router
from .models import  Product , Address



commerce_controllers = Router()

@commerce_controllers.get("products")
def fetch_products(request):
    result= Product.objects.values()
    list_result = [p for p in result] 
    return list_result


@commerce_controllers.get("addresses")
def fetch_address(request):
    result= Address.objects.values()
    list_result = [p for p in result] 
    return list_result


@commerce_controllers.get("related")
def related_model_data(request):

    result= Product.objects.select_related("category").values('name','category__name','category__image')  
    list_result = [p for p in result] 
    return list_result










