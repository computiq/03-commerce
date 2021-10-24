
from ninja import Router
from commerce.models import Product,Address


controller= Router()
# Create your views here.

 
@controller.get('Products')
def showingProducts(request):
    return list(Product.objects.values())

@controller.get('Address')
def showingAddress(request):
    return list(Address.objects.values())

    



