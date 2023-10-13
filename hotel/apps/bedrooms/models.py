from django.db import models
#from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from django.db.models.signals import pre_save
from django.dispatch import receiver


TYPE_CHOICES = (
    ('Habitación Simple', 'Habitación Simple'),
    ('Habitación Doble', 'Habitación Doble'),
    ('Habitación Triple', 'Habitación Triple'),
    ('Habitación Matrimonial', 'Habitación Matrimonial'),
    )

class Bedroom(BaseModel):

    description=models.CharField(max_length=30, choices=TYPE_CHOICES)
    image=models.ImageField('Imagen de la Habitacion',upload_to='bedrooms/',blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    availability=models.BooleanField('Estado',default=True)
    
    class Meta:
        verbose_name='Bedroom'
        verbose_name_plural='Bedrooms'

    def __str__(self):
        return self.description


@receiver(pre_save, sender=Bedroom)
def update_price(sender, instance, **kwargs):
    # Define los precios correspondientes a cada tipo de habitación
    prices = {
        'Habitación Simple': 700.00,
        'Habitación Doble': 1200.00,
        'Habitación Triple': 2000.00,
        'Habitación Matrimonial': 2500.00,
    }
  
    instance.price = prices.get(instance.description, 0.00)