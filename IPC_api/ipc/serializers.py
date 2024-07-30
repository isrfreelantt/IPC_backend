from rest_framework import serializers
from .models import *

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class Car_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spec
        fields = '__all__'

class CoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coverage
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    coverages = CoverageSerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = ['id', 'package_type', 'name', 'company', 'coverages']

class PremiumSerializer(serializers.ModelSerializer):
    package = PackageSerializer(read_only=True)

    class Meta:
        model = Premium
        fields = ['package', 'min_sum_insured', 'max_sum_insured', 'premium', 'premium_total', 'deduct', 'garage', 'insurance_type', 'cctv']

class CarOwnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_Owned
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'