from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('AutoTechApi.car.urls'))
]
