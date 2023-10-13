from rest_framework import serializers

from apps.bedrooms.models import Bedroom

class BedroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bedroom
        exclude = ('state','create_date','modified_date','delete_date')


    def to_representation(self,instance):
        return {
            'id': instance.id,         
            'description': instance.description,
            'image': instance.image.url if instance.image != '' else '',
            'price': instance.price,
            'availability':instance.availability
        }

class BedroomRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bedroom
        exclude = ('state','create_date','modified_date','delete_date') 