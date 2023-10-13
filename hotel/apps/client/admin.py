from django.contrib import admin
from apps.client.models import *

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','nationality','type_client')


admin.site.register(Client,ClientAdmin)

