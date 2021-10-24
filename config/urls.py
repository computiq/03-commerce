from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from commerce.controllers import test_api
from ninja import NinjaAPI
from commerce.controllers import product_controller, address_controller
from django.urls import path, include


api = NinjaAPI(
    version='1.0.0',
    title='client API v1',
    description='API documentation',
)

api.add_router('/test', test_api)
api.add_router('/Product', product_controller)
api.add_router('/Address', address_controller)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
