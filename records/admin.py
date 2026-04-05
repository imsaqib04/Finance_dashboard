from django.contrib import admin
from .models import FinancialRecord

@admin.register(FinancialRecord)
class FinancialRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'record_type', 'amount', 'category', 'date', 'created_by', 'is_deleted')
    list_filter = ('record_type', 'is_deleted', 'date')
    search_fields = ('category', 'notes')