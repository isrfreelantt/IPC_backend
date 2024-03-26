from rest_framework import generics
from rest_framework.response import Response
from .models import Car, Car_detail, Campaign, Coverage, Premium
from .serializers import CarSerializer, Car_detailSerializer, CampaignSerializer, CoverageSerializer, PremiumSerializer

class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarsByBrand(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        brand = self.kwargs['brand']  # Retrieve name from URL
        return Car.objects.filter(brand=brand)

class UniqueBrand(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        queryset = Car.objects.order_by('brand').distinct('brand').values_list('brand', flat=True)
        return Response(queryset)
    
class CarDetailList(generics.ListAPIView):
    serializer_class = Car_detailSerializer

    def get_queryset(self):
        queryset = Car_detail.objects.all()
        year = self.request.query_params.get('year')
        model = self.request.query_params.get('model')

        queryset = Car_detail.objects.all()

        if year:
            queryset = queryset.filter(year=year)
        
        if model:
            queryset = queryset.filter(model=model)
        
        return queryset

class CampaignList(generics.ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    
class CoverageList(generics.ListAPIView):
    queryset = Coverage.objects.all()
    serializer_class = CoverageSerializer
    
class PremiumList(generics.ListAPIView):
    queryset = Premium.objects.all()
    serializer_class = PremiumSerializer

class PremiumByCar(generics.ListAPIView):
    serializer_class = PremiumSerializer

    def get_queryset(self):
        # Get the model_id from the URL query parameters
        model_id = self.request.query_params.get('model_id')
        # year = self.request.query_params.get('year')

        # if year:
        #     queryset = queryset.filter(year=year)

        # Retrieve Premium objects filtered by the specified model_id
        if model_id is not None:
            premium_queryset = Premium.objects.filter(cars__id=model_id)
            return premium_queryset
        else:
            # Handle case where model_id is not provided
            return Premium.objects.none()