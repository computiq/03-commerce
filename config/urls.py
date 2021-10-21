from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from commerce.controllers import commerce_controller
api = NinjaAPI(
    title='E-commerce API',
)

api.add_router('commerce_controller',commerce_controller)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),

]