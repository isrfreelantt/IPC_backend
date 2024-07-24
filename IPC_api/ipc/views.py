from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import *
from .serializers import *
from .data_manager import DataManager

class CarList(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        brand = self.request.query_params.get('brand')
        year = self.request.query_params.get('year')

        queryset = Car.objects.all()

        # Ensure all required parameters are provided
        if not brand or not year:
            return Response({"error": "Missing required query parameters"}, status=status.HTTP_400_BAD_REQUEST)

        if brand:
            queryset = queryset.filter(brand_code=brand)
        
        if year:
            queryset = queryset.filter(min_year__lte=year, max_year__gte=year)      

        return queryset

class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
class CarSpecList(generics.ListAPIView):
    serializer_class = Car_detailSerializer

    def get_queryset(self):
        queryset = Spec.objects.all()

        # Extract query parameters
        model_code = self.request.query_params.get('model')
        model_year = self.request.query_params.get('year')

        # Ensure all required parameters are provided
        if not model_code or not model_year:
            return Response({"error": "Missing required query parameters"}, status=status.HTTP_400_BAD_REQUEST)

        # Filter by year
        if model_year:
            queryset = queryset.filter(year=model_year)
        
        # Filter by model
        if model_code:
            queryset = queryset.filter(model_code=model_code)
        
        return queryset

class ChubbSpecList(APIView):
    def get(self, request):
        # Extract query parameters
        brand_code = request.query_params.get('brand')
        model_code = request.query_params.get('model')
        model_year = request.query_params.get('year')

        # Ensure all required parameters are provided
        if not brand_code or not model_code or not model_year:
            return Response({"error": "Missing required query parameters"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Initialize the DataManager
        data_manager = DataManager()

        try:
            vehicle_specs = data_manager.extract_car_specs(brand_code, model_code, model_year)
            return Response(vehicle_specs, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PackageList(generics.ListAPIView):
    serializer_class = PackageSerializer

    def get_queryset(self):
        ids = self.request.query_params.get('id')

        queryset = Package.objects.all()

        if ids:
            id_list = ids.split(',')  # Split id to list
            queryset = Package.objects.filter(pk__in=id_list)
        
        return queryset

class CoverageList(generics.ListAPIView):
    serializer_class = CoverageSerializer

    def get_queryset(self):
        package = self.request.query_params.get('package_id')

        queryset = Coverage.objects.all()

        if package:
            package_list = package.split(',')  # Split id to list
            queryset = queryset.filter(package__in=package_list)
        
        return queryset

class PremiumList(generics.ListAPIView):
    queryset = Premium.objects.all()
    serializer_class = PremiumSerializer

class PremiumByCar(generics.ListAPIView):
    serializer_class = PremiumSerializer

    def get_queryset(self):
        # Get the model_id from the URL query parameters
        model_id = self.request.query_params.get('model_id')
        year = self.request.query_params.get('year')
        sum_insured = self.request.query_params.get('sum_insured')
        province = self.request.query_params.get('province')
        insurance_type = self.request.query_params.get('insurance_type')

        # Retrieve Premium objects filtered by the specified model_id
        queryset = Premium.objects.all()
        
        if insurance_type:
            try:
                queryset = queryset.filter(insurance_type=insurance_type)
            except ValueError:
                pass

        # Filter by age
        if year:
            try:
                # Calculate age by dynamic current year
                age = timezone.now().year - int(year)
                queryset = queryset.filter(min_age__lte=age, max_age__gte=age)
            except ValueError:
                pass
        
        # Filter by sum insured
        if sum_insured:
            try:
                sum_insured = int(sum_insured)
                queryset = queryset.filter(min_sum_insured__lte=sum_insured, max_sum_insured__gte=sum_insured)
            except ValueError:
                pass
        
        if province:
            try:
                if province == 'กรุงเทพมหานคร':
                    area = 'Bangkok Metropolitan Region'
                else:
                    area = 'Upcountry'
                # Apply the area filter
                area_queryset = queryset.filter(location=area)

                # null_location_queryset = queryset.filter(location__isnull=True)
                null_location_queryset = queryset.filter(location='')

                queryset = area_queryset | null_location_queryset

            except ValueError:
                pass
    
        # Filter by model_id
        if model_id:
            premium_queryset = queryset.filter(cars=model_id)

            return premium_queryset
        else:
            # Handle case where model_id is not provided
            return Premium.objects.none()
        
class CombinedPremium(generics.ListAPIView):
    serializer_class = PremiumSerializer

    def get(self, request):
        model_id = request.query_params.get('model_id')
        year = request.query_params.get('year')
        sum_insured = request.query_params.get('sum_insured')
        insurance_type = request.query_params.get('insurance_type')
        voluntary_code = request.query_params.get('voluntary_code')
        vehicle_key = request.query_params.get('vehicle_key')
        province = request.query_params.get('province')

        queryset = Premium.objects.all()

        if insurance_type:
            try:
                queryset = queryset.filter(insurance_type=insurance_type)
            except ValueError:
                pass

        if year:
            try:
                age = timezone.now().year - int(year)
                queryset = queryset.filter(min_age__lte=age, max_age__gte=age)
            except ValueError:
                pass

        if sum_insured:
            try:
                sum_insured = int(sum_insured)
                # Min less than or equal to Sum insured and Max greater than or equal to 90% Sum insured
                queryset = queryset.filter(min_sum_insured__lte=sum_insured)
                queryset = queryset.filter(max_sum_insured__gte=sum_insured*9/10)

            except ValueError:
                pass

        if province:
            try:
                if province == 'กรุงเทพมหานคร':
                    area = 'Bangkok'
                else:
                    area = 'Upcountry'
                # Apply the area filter
                area_queryset = queryset.filter(location=area)

                # null_location_queryset = queryset.filter(location__isnull=True)
                null_location_queryset = queryset.filter(location='')

                queryset = area_queryset | null_location_queryset

            except ValueError:
                pass

        if model_id:
            premium_queryset = queryset.filter(cars=model_id)
            # Initialize DataManager
            data_manager = DataManager()
            
            # Fetch the package data
            try:
                extracted_package = data_manager.extract_package(insurance_type, voluntary_code, vehicle_key, province)
            except Exception as e:
                return Response({"error": str(e)}, status=500)

            # Serialize premium data
            premium_data = PremiumSerializer(premium_queryset, many=True).data

            # Combine the data
            combined_data = {
                "Database_package": premium_data,
                "API_package": extracted_package
            }

            return Response(combined_data)
        else:
            # Handle case where model_id is not provided
            return Response({"error": "model_id is required"}, status=400)

class CarOwnedListCreate(generics.ListCreateAPIView):
    queryset = Car_Owned.objects.all()
    serializer_class = CarOwnedSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProvinceList(generics.ListAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer