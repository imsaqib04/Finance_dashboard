from records.models import FinancialRecord

class DashboardSummary(FinancialRecord):
    class Meta:
        proxy = True
        verbose_name = 'Dashboard Summary'
        verbose_name_plural = 'Dashboard Summaries'