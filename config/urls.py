from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from commerce.controllers import products_controller, addresses_controller

api = NinjaAPI()
api.add_router('products', products_controller )
api.add_router('addresses', addresses_controller )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]