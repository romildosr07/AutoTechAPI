from django.contrib import admin

from AutoTechApi.client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'cellphone')
