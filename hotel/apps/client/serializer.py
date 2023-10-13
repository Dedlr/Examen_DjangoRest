from rest_framework import serializers

from apps.client.models import Client

class CLientSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Client
        exclude = ('state','create_date','modified_date','delete_date')


    def to_representation(self,instance):
        return {
            'id': instance.id,         
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'dpi_pasaporte':instance.dpi_pasaporte,
            'email':instance.email,
            'nationality': instance.nationality,
            'type_client':instance.type_client
        }

class ClientRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Client
        exclude = ('state','create_date','modified_date','delete_date') 