from django.contrib import admin
from .models import DashboardSummary
from .services import get_dashboard_summary

@admin.register(DashboardSummary)
class DashboardSummaryAdmin(admin.ModelAdmin):
    
    change_list_template = 'admin/dashboard_summary.html'

    def changelist_view(self, request, extra_context=None):
        # 1. Database se live summary calculate karo
        summary_data = get_dashboard_summary()
        
        # 2. Ye data HTML page (template) ko bhej do
        extra_context = extra_context or {}
        extra_context['title'] = 'Financial Analytics Summary'
        extra_context['summary'] = summary_data
        
        return super().changelist_view(request, extra_context=extra_context)