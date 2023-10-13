from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bedrooms/',include('apps.bedrooms.router')),
    path('clients/',include('apps.client.router')),
    path('reservations/',include('apps.reservation.router')),
]
