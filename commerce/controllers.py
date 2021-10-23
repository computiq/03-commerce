from django.shortcuts import render
from ninja import Router
from commerce.models import Product, Order, Item, Address, OrderStatus, ProductImage, City, Category, Merchant, Vendor, Label, User

commerce_controller=Router()



@commerce_controller.get('/Product')
def display_products(request):
	Products = list(Product.objects.values())
	Merchants = list(Merchant.objects.values())
	Categories = list(Category.objects.values())
	Vendors = list(Vendor.objects.values())
	Labels = list(Label.objects.values())

# return name of related data instead id
	for i in range(len(Products)):

		for j in range(len(Merchants)):
			if Products[i]['merchant_id'] == Merchants[j]['id']:
				Products[i]['merchant_id']=Merchants[j]['name']

		for j in range(len(Categories)):
			if Products[i]['category_id'] == Categories[j]['id']:
				Products[i]['category_id']=Categories[j]['name']

		for j in range(len(Vendors)):
			if Products[i]['vendor_id'] == Vendors[j]['id']:
				Products[i]['vendor_id']=Vendors[j]['name']

		for j in range(len(Labels)):
			if Products[i]['label_id'] == Labels[j]['id']:
				Products[i]['label_id']=Labels[j]['name']

	return Products


@commerce_controller.get('/Address')
def display_address(request):
	address = list(Address.objects.values())
	cities = list(City.objects.values())

	for i in range(len(address)):

		for j in range(len(cities)):
			if address[i]['city_id'] == cities[j]['id']:
				address[i]['city_id']=cities[j]['name']
	return address



