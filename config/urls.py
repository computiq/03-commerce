
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from  commerce.controllers import commerce_controller

api = NinjaAPI()

api.add_router('commerce',commerce_controller)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),

]
