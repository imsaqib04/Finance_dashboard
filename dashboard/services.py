from django.db.models import Sum
from records.models import FinancialRecord

def get_dashboard_summary():
    # Sirf active records par calculation (Soft deleted ignore honge)
    active_records = FinancialRecord.objects.filter(is_deleted=False)
    
    # DB level Aggregations (Python loops use nahi kiye, jo ki highly scalable hai)
    total_income = active_records.filter(record_type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = active_records.filter(record_type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
    
    net_balance = total_income - total_expense
    
    # Category wise total expenses
    expense_by_category = list(
        active_records.filter(record_type='EXPENSE')
        .values('category')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": net_balance,
        "expense_by_category": expense_by_category
    }