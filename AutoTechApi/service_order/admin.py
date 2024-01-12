from django.contrib import admin

from AutoTechApi.service_order.models import Part, Service, ServiceOrder


@admin.register(Part)
class PartModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'stock_quantity', 'car_make')
    search_fields = ['name']

    @admin.display(description='Marca')
    def car_make(self, obj):
        return obj.car_make.name


@admin.register(Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'is_active')
    search_fields = ['name']


@admin.register(ServiceOrder)
class ServiceOrderModelAdmin(admin.ModelAdmin):
    list_display = ('car_plate', 'is_active', 'created_at')
    search_fields = ['name']
    filter_horizontal = ('service', 'part')

    @admin.display(description='Placa')
    def car_plate(self, obj):
        return obj.car.license_plate
