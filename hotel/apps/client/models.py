""" Model Client"""
from django.db import models
from apps.base.models import BaseModel

TYPE_CLIENT = (
    ('Comun', 'Comun'),
    ('Coorporativo', 'Coorporativo'),
    )

TYPE_NATIONALITY = (
    ('Local', 'Local'),
    ('Extranjero', 'Extranjero'),
    )


class Client(BaseModel):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dpi_pasaporte = models.CharField(max_length=20)
    nit = models.CharField(max_length=15)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    adress = models.CharField(max_length=255)
    nationality = models.CharField(max_length=30, choices=TYPE_NATIONALITY)
    type_client= models.CharField(max_length=30, choices=TYPE_CLIENT)
    
    class Meta:
        verbose_name='Client'
        verbose_name_plural='Clients'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


