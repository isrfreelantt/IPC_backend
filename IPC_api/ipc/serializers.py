from rest_framework import serializers
from .models import Car, Car_detail, Campaign, Coverage, Premium, Car_Owned, Customer

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class Car_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_detail
        fields = '__all__'

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class CoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coverage
        fields = '__all__'

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