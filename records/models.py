from django.db import models
from django.conf import settings

class FinancialRecord(models.Model):

    class RecordType(models.TextChoices):  
        INCOME = 'INCOME', 'Income'
        EXPENSE = 'EXPENSE', 'Expense'

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    record_type = models.CharField(max_length=10, choices=RecordType.choices) 
    category = models.CharField(max_length=50, db_index=True)
    date = models.DateField(db_index=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.record_type} - {self.amount} on {self.date}"