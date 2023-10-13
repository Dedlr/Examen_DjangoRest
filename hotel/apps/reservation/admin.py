from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('client', 'type_bedroom', 'entry_date', 'exit_date', 'total_cost')

admin.site.register(Reservation, ReservationAdmin)
