from django.contrib import admin

from AutoTechApi.car.models import CarMake, CarModel, Car


@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    search_fields = ['name']


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    search_fields = ['name']


@admin.register(Car)
class Car(admin.ModelAdmin):
    list_display = ('license_plate', 'vehicle', 'kilometers')
    search_fields = ['licence_plate']

    @admin.display(description='Veículo')
    def vehicle(self, obj):
        make_model = f'{obj.car_make.name} - {obj.car_model.name}'
        return make_model
