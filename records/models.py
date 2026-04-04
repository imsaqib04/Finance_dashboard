from django.db import models

class FinancialRecord(models.Model):
    TYPE_CHOICES = (
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    )
    
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    record_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=50, db_index=True)
    date = models.DateField(db_index=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False) # Soft delete mechanism

    def __str__(self):
        return f"{self.record_type} - {self.amount} on {self.date}"