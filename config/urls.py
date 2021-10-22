from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from account.controller import account_controller
from commerce.controllers import commerce_controller

api = NinjaAPI()

api.add_router('', account_controller)
api.add_router('', commerce_controller)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
