from rest_framework import serializers
from electronics.models import Product, Supplier
from electronics.validators import SimultaneousSelectionValidator


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, required=False)
    validators = [SimultaneousSelectionValidator(network_level='network_level', supply='supply')]

    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierUpdateSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, required=False)
    validators = [SimultaneousSelectionValidator(network_level='network_level', supply='supply')]

    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ['debt_to_supplier']
