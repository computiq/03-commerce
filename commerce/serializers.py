from rest_framework.serializers import ModelSerializer
from commerce.models import Address, Product


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
