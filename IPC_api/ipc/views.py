from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status
from .data_manager import DataManager

class CarList(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        brand = self.request.query_params.get('brand')
        year = self.request.query_params.get('year')

        queryset = Car.objects.all()

        if brand:
            queryset = queryset.filter(brandcode=brand)
        
        if year:
            queryset = queryset.filter(min_year__lte=year, max_year__gte=year)      

        return queryset

class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
class CarSpecList(APIView):
    def get(self, request):
        # Extract query parameters
        brand_code = request.query_params.get('brand')
        model_code = request.query_params.get('model')
        model_year = request.query_params.get('year')

        # Ensure all required parameters are provided
        if not brand_code or not model_code or not model_year:
            return Response({"error": "Missing required query parameters"}, status=status.HTTP_400_BAD_REQUEST)

        # Initialize the TokenManager
        data_manager = DataManager()

        try:
            vehicle_specs = data_manager.extract_car_specs(brand_code, model_code, model_year)
            return Response(vehicle_specs, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CampaignList(generics.ListAPIView):
    serializer_class = CampaignSerializer

    def get_queryset(self):
        ids = self.request.query_params.get('id')

        queryset = Campaign.objects.all()

        if ids:
            id_list = ids.split(',')  # Split id to list
            queryset = Campaign.objects.filter(pk__in=id_list)
        
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