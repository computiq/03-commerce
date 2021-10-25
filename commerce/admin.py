from django.contrib import admin

from commerce.models import Product, Order, Item, Address, OrderStatus, ProductImage, City, Category, Vendor, Merchant, Label

admin.site.register(Address)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Item)
admin.site.register(Label)
admin.site.register(Merchant)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Vendor)