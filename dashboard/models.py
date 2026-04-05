from records.models import FinancialRecord

class DashboardSummary(FinancialRecord):
    class Meta:
        proxy = True  # Ye batata hai ki naya table create nahi karna
        verbose_name = 'Dashboard Summary'
        verbose_name_plural = 'Dashboard Summaries'