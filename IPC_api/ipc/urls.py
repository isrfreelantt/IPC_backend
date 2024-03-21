from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarList.as_view(), name='car-list'),
    path('subcars/', views.CarDetailList.as_view(), name='subcar-list'),
    path('campaign/', views.CampaignList.as_view(), name='campaign-list'),
    path('coverage/', views.CoverageList.as_view(), name='coverage-list'),
    path('premium/', views.PremiumList.as_view(), name='premium-list'),
    path('premium_car/', views.Premium_CarList.as_view(), name='premium_car-list'),

]