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
        model = Car_detail
        fields = '__all__'

class CoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coverage
        fields = '__all__'

class CampaignSerializer(serializers.ModelSerializer):
    coverages = CoverageSerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = ['id', 'insurance_type', 'name', 'company', 'coverages']

class PremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premium
        fields = ['min_sum_insured', 'max_sum_insured', 'premium', 'campaign', 'min_age', 'max_age', 'deduct', 'garage']

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