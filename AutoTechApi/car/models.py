import uuid

from django.db import models
from AutoTechApi.client.models import Client


class CarMake(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Marca', max_length=100)

    is_active = models.BooleanField('Ativo',default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        db_table = 'car_make'
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'

    def __str__(self):
        return f'{self.name}' if self.name is not None else ''


class CarModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Modelo', max_length=100)

    is_active = models.BooleanField('Ativo',default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        db_table = 'car_model'
        verbose_name = 'modelo'
        verbose_name_plural = 'modelos'

    def __str__(self):
        return f'{self.name}' if self.name is not None else ''


class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    license_plate = models.CharField('Placa', max_length=10, unique=True)
    kilometers = models.IntegerField('KM')

    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT, verbose_name='marca')
    car_model = models.ForeignKey(CarModel, on_delete=models.PROTECT, verbose_name='modelo')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='client')

    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        db_table = 'car'
        verbose_name = 'carro'
        verbose_name_plural = 'carros'

    def __str__(self):
        return f'{self.license_plate}' if self.license_plate is not None else ''
