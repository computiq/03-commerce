from ninja import Router
from commerce.models import Product, Address

product_controller = Router()
address_controller = Router()

# for the extra sub-task
@product_controller.get('')
def list_products(request):
  return list(Product.objects.select_related('category').values('name', 'qty', 'discounted_price', 'category__name'))

# get all addresses
@address_controller.get('')
def list_addresses(request):
  return list(Address.objects.values(''))
  '''
  for retrieving only specific attributes just pass their names in values as arguments
  return list(Address.objects.values('phone'))
  '''