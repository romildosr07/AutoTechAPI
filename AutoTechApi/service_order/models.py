import uuid

from django.db import models

from AutoTechApi.car.models import Car, CarMake


class Part(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Peça", max_length=100)
    value = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    stock_quantity = models.IntegerField(default=0)

    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT, verbose_name='marca', null=True, blank=True)

    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        db_table = 'part'
        verbose_name = 'peça'
        verbose_name_plural = 'peças'

    def __str__(self):
        return f'{self.name}' if self.name is not None else ''


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Serviço", max_length=100)
    value = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        db_table = 'service'
        verbose_name = 'serviço'
        verbose_name_plural = 'serviços'

    def __str__(self):
        return f'{self.name}' if self.name is not None else ''


class ServiceOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    service = models.ManyToManyField(Service, verbose_name='serviço')
    part = models.ManyToManyField(Part, verbose_name='peça')
    car = models.ForeignKey(Car, on_delete=models.PROTECT, verbose_name='carro', null=True, blank=True)

    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        db_table = 'service_order'
        verbose_name = 'Ordem de serviço'
        verbose_name_plural = 'Ordem de serviços'

    def __str__(self):
        return f'{self.car.license_plate}' if self.car.license_plate is not None else ''
