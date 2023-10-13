from rest_framework import serializers

from apps.reservation.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Reservation
        exclude = ('state','create_date','modified_date','delete_date')


    def to_representation(self,instance):
        return {
            'id': instance.id,         
            'client': instance.client.first_name,
            'type_bedroom': instance.type_bedroom.description,
            'total_days':instance.total_days,
            'cost':instance.cost,
            'total_cost':instance.total_cost
        }

class ReservationRetriveSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Reservation
        exclude = ('state','create_date','modified_date','delete_date') 