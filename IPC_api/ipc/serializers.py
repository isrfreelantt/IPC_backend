from rest_framework import serializers
from .models import Car, Car_detail, Campaign, Coverage, Premiums

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
        model = Premiums
        fields = '__all__'

