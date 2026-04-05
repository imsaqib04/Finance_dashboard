from django.contrib import admin
from django import forms
from django.utils.timezone import localdate
from .models import FinancialRecord

class FinancialRecordForm(forms.ModelForm):
    class Meta:
        model = FinancialRecord
        fields = '__all__'
        widgets = {
            'amount': forms.NumberInput(attrs={'min': '0.01', 'step': '0.01'}),
            
            'date': forms.DateInput(attrs={'type': 'date', 'max': localdate().strftime('%Y-%m-%d')})
        }

@admin.register(FinancialRecord)
class FinancialRecordAdmin(admin.ModelAdmin):
    form = FinancialRecordForm  # <-- Custom form yahan attach kiya
    list_display = ('id', 'record_type', 'amount', 'category', 'date', 'is_deleted')
    list_filter = ('record_type', 'is_deleted', 'date')
    search_fields = ('category', 'notes')