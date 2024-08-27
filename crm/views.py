from rest_framework import generics
from .models import Customer, Sales
from .serializers import CustomerSerializer, SalesSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SalesListCreateView(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class SalesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
