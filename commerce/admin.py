from django.contrib import admin


from commerce.models import Merchant, Product, Order, Item, Address, OrderStatus, ProductImage, City, Category, Vendor

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Address)
admin.site.register(OrderStatus)
admin.site.register(ProductImage)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Merchant)