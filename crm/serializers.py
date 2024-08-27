from rest_framework import serializers
from .models import Customer, Sales

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'
