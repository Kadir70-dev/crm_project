# reports/services.py
from crm.models import Sales
from django.db.models import Sum, Count
import datetime

def generate_sales_report():
    today = datetime.date.today()
    monthly_sales = Sales.objects.filter(date__year=today.year, date__month=today.month)
    total_sales = monthly_sales.aggregate(total=Sum('amount'))
    total_transactions = monthly_sales.count()
    
    return {
        "total_sales": total_sales['total'],
        "total_transactions": total_transactions,
        "sales_by_product": monthly_sales.values('product').annotate(total_amount=Sum('amount')).order_by('-total_amount'),
    }
