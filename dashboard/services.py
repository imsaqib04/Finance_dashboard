from django.db.models import Sum
from django.db.models.functions import TruncMonth
from records.models import FinancialRecord

def _get_total(queryset, record_type):
    return queryset.filter(record_type=record_type).aggregate(
        total=Sum('amount')
    )['total'] or 0

def _get_expense_by_category(queryset):
    return list(
        queryset.filter(record_type=FinancialRecord.RecordType.EXPENSE)
        .values('category')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

def _get_monthly_trends(queryset):
    return list(
        queryset
        .annotate(month=TruncMonth('date'))
        .values('month', 'record_type')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

def _get_recent_activity(queryset, limit=10):
    return list(
        queryset
        .select_related('created_by')
        .order_by('-date')[:limit]
        .values('id', 'record_type', 'amount', 'category', 'date', 'created_by__username')
    )

def get_dashboard_summary():
    active_records = FinancialRecord.objects.filter(is_deleted=False)

    total_income = _get_total(active_records, FinancialRecord.RecordType.INCOME)
    total_expense = _get_total(active_records, FinancialRecord.RecordType.EXPENSE)

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense,
        "expense_by_category": _get_expense_by_category(active_records),
        "monthly_trends": _get_monthly_trends(active_records),
        "recent_activity": _get_recent_activity(active_records),
    }