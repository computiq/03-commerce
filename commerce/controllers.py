from django.shortcuts import render
from ninja import Router
from commerce.models import Product, Order, Item, Address, OrderStatus, ProductImage, City, Category, Merchant

commerce_controller=Router()



@commerce_controller.get('/Product')
def display_products(request):
	Products= list(Product.objects.values())
	Merchants= list(Merchant.objects.values())

# return name of merchants instead id

	for i in range(len(Products)):
		for j in range(len(Merchants)):
			if Products[i]['merchant_id'] == Merchants[j]['id']:
				Products[i]['merchant_id']=Merchants[j]['name']
	return Products


@commerce_controller.get('/Address')
def display_address(request):
	return list(Address.objects.values())



