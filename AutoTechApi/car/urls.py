from django.contrib import admin
from django.urls import path

from AutoTechApi.car.views import CarViewSet, CarMakeViewSet

urlpatterns = [
    path('', CarViewSet.as_view(), name='car'),
    path('car-make/', CarMakeViewSet.as_view(), name='car_make')
]
