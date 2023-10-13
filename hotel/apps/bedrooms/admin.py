from django.contrib import admin
from apps.bedrooms.models import *

# Register your models here.
class BedroomAdmin(admin.ModelAdmin):
    list_display = ('id','description','price','availability')


admin.site.register(Bedroom,BedroomAdmin)
