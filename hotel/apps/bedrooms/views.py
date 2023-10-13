from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


from apps.base.utils import validate_files
from apps.bedrooms.serializer import (
    BedroomSerializer,BedroomRetrieveSerializer
)

class BedroomViewSet(viewsets.ModelViewSet):
    serializer_class = BedroomSerializer
  
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
        data = validate_files(request.data,'image')
        serializer = self.serializer_class(data=data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Habitacion creada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        bedroom = self.get_queryset(pk)
        if bedroom:
            bedroom_serializer = BedroomRetrieveSerializer(bedroom)
            return Response(bedroom_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'No existe una Habitacion con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            data = validate_files(request.data, 'image', True)
            bedroom_serializer = self.serializer_class(self.get_queryset(pk), data=data)            
            if bedroom_serializer.is_valid():
                bedroom_serializer.save()
                return Response({'message':'Habitacion actualizada correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':bedroom_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        bedroom = self.get_queryset().filter(id=pk).first() # get instance        
        if bedroom:
            bedroom.state = False
            bedroom.save()
            return Response({'message':'Habitacion eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe una Habitacion con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
    



