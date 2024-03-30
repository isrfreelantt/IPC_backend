from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *

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
    serializer_class = CampaignSerializer

    def get_queryset(self):
        ids = self.request.query_params.get('id')

        queryset = Campaign.objects.all()

        if ids:
            id_list = ids.split(',')  # Split id to list
            queryset = queryset.filter(id__in=id_list)
        
        return queryset
        
    
class CoverageList(generics.ListAPIView):
    serializer_class = CoverageSerializer

    def get_queryset(self):
        campaign = self.request.query_params.get('campaign_id')

        queryset = Coverage.objects.all()

        if campaign:
            campaign_list = campaign.split(',')  # Split id to list
            queryset = queryset.filter(campaign__in=campaign_list)
        
        return queryset

class PremiumList(generics.ListAPIView):
    queryset = Premium.objects.all()
    serializer_class = PremiumSerializer

class PremiumByCar(generics.ListAPIView):
    serializer_class = PremiumSerializer

    def get_queryset(self):
        # Get the model_id from the URL query parameters
        model_id = self.request.query_params.get('model_id')
        age = self.request.query_params.get('age')
        sum_Insured = self.request.query_params.get('sum_insured')

        # Retrieve Premium objects filtered by the specified model_id
        queryset = Premium.objects.all()

        if age:
            queryset = queryset.filter(min_age__lte=age, max_age__gte=age)
        
        if sum_Insured:
            queryset = queryset.filter(min_sum_insured__lte=sum_Insured, max_sum_insured__gte=sum_Insured)

        if model_id is not None:
            premium_queryset = queryset.filter(cars__id=model_id)
            return premium_queryset
        else:
            # Handle case where model_id is not provided
            return Premium.objects.none()

class CarOwnedListCreate(generics.ListCreateAPIView):
    queryset = Car_Owned.objects.all()
    serializer_class = CarOwnedSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProvinceList(generics.ListAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer