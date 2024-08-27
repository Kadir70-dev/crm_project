from django.urls import path
from .views import CustomerListCreateView, CustomerDetailView, SalesListCreateView, SalesDetailView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('sales/', SalesListCreateView.as_view(), name='sales-list-create'),
    path('sales/<int:pk>/', SalesDetailView.as_view(), name='sales-detail'),
]
