# reports/urls.py
from django.urls import path
from .views import SalesReportView

urlpatterns = [
    path('sales-report/', SalesReportView.as_view(), name='sales-report'),
]
