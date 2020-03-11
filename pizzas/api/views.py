from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
    )
from pizzas.models import Pizza
from .serializers import PizzaSerializer, PizzaMiniSerializer
from rest_framework.response import Response
from rest_framework import status


class PizzaListAPIView(ListCreateAPIView):
    queryset = Pizza.objects.all().order_by('-votes')
    serializer_class = PizzaSerializer
    

class PizzaRUDView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PizzaSerializer
    
    def get_queryset(self):
        return Pizza.objects.all().order_by('-votes')
    
    
class PizzaVoteView(UpdateAPIView):
    lookup_field = 'id'
    serializer_class = PizzaMiniSerializer
    
    def get_queryset(self):
        return Pizza.objects.all()
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.votes = int(instance.votes) + 1
        instance.save()

        serializer = PizzaMiniSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
