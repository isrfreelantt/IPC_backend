from rest_framework import generics
from .models import Car, Car_detail, Campaign, Coverage, Premiums
from .serializers import CarSerializer, Car_detailSerializer, CampaignSerializer, CoverageSerializer, PremiumSerializer

class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailList(generics.ListAPIView):
    queryset = Car_detail.objects.all()
    serializer_class = Car_detailSerializer

class CampaignList(generics.ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    
class CoverageList(generics.ListAPIView):
    queryset = Coverage.objects.all()
    serializer_class = CoverageSerializer
    
class PremiumList(generics.ListAPIView):
    queryset = Premiums.objects.all()
    serializer_class = PremiumSerializer
    
