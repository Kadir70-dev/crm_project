# reports/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from crm.models import Sales
from .services import generate_sales_report

class SalesReportView(APIView):
    def get(self, request):
        report = generate_sales_report()
        return Response(report)
