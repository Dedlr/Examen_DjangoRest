from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from apps.reservation.serializer import ReservationSerializer,ReservationRetriveSerializer

class ReservationViewSet(viewsets.ModelViewSet):

    serializer_class = ReservationSerializer
  
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        bedroom_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": bedroom_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request): 
        serializer = self.serializer_class(data=request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Reserva registrada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        reservation = self.get_queryset(pk)
        if reservation:
           client_serializer = ReservationRetriveSerializer(reservation)
           return Response(client_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'No existe un cliente con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            reservation_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if reservation_serializer.is_valid():
                reservation_serializer.save()
                return Response({'message':'Reserva actualizada correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':reservation_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        reservation = self.get_queryset().filter(id=pk).first()       
        if reservation:
           reservation.state = False
           reservation.save()
        return Response({'message':'Reserva eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe una reserva con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
