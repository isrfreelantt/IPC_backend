from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarList.as_view(), name='car-list'),
    path('brands/', views.BrandList.as_view(), name='brand'),
    path('car-details/', views.CarSpecList.as_view(), name='car-detail-list'),
    path('campaigns/', views.CampaignList.as_view(), name='campaign-list'),
    path('coverage/', views.CoverageList.as_view(), name='coverage-list'),
    path('premiums/', views.PremiumByCar.as_view(), name='premium-by-car'),
    path('cars-owned/', views.CarOwnedListCreate.as_view(), name='car-owned-list-create'),
    path('customer/', views.CustomerListCreate.as_view(), name='customer-list-create'),
    path('province/', views.ProvinceList.as_view(), name='province-list'),
]