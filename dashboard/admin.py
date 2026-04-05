from django.contrib import admin
from .models import DashboardSummary
from .services import get_dashboard_summary

@admin.register(DashboardSummary)
class DashboardSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/dashboard_summary.html'

    def changelist_view(self, request, extra_context=None):
        summary_data = get_dashboard_summary()
        extra_context = extra_context or {}
        extra_context['title'] = 'Financial Analytics Summary'
        extra_context['summary'] = summary_data
        return super().changelist_view(request, extra_context=extra_context)

    def has_add_permission(self, request):
        return False  

    def has_change_permission(self, request, obj=None):
        return False 

    def has_delete_permission(self, request, obj=None):
        return False  