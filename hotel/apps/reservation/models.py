""" Model Reservation"""
from django.db import models
from apps.base.models import BaseModel
from django.db.models.signals import pre_save
from django.dispatch import receiver



from apps.client.models import Client
from apps.bedrooms.models import Bedroom

TYPE_PAY= (
('Tarjeta', 'Tarjeta'),
('Efectivo', 'Efectivo'),
)


class Reservation(BaseModel):

    client=models.ForeignKey(Client,on_delete=models.CASCADE, null=False, blank=True)
    type_bedroom= models.ForeignKey(Bedroom, on_delete=models.CASCADE, null=False, blank=True)
    payment_method=models.CharField(max_length=30, choices=TYPE_PAY)
    entry_date=models.DateField()
    exit_date=models.DateField()
    total_days = models.PositiveIntegerField(default=0)
    n_adults= models.PositiveIntegerField(default=0)
    n_children= models.PositiveIntegerField(default=0)
    n_total=models.PositiveIntegerField(default=0, editable=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)

    class Meta:
        verbose_name='Reservation'
        verbose_name_plural='Reservations'

    def update_total_guests(self):
        # Calcular el total de huespedes
        self.n_total = self.n_adults + self.n_children

    def save(self, *args, **kwargs):
        # Costo de la habitacion
        self.cost = self.type_bedroom.price
            
       # Costo total
        self.total_cost = self.total_days*self.type_bedroom.price


        super().save(*args, **kwargs)

@receiver(pre_save, sender=Reservation)
def update_reservation(sender, instance, **kwargs):

    instance.update_total_guests()