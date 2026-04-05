from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from decimal import Decimal

# Custom validator: Future date ko block karne ke liye
def validate_past_or_today(value):
    if value > timezone.now().date():
        raise ValidationError("Future dates are not allowed. Please select today or a past date.")

class FinancialRecord(models.Model):

    class RecordType(models.TextChoices):  
        INCOME = 'INCOME', 'Income'
        EXPENSE = 'EXPENSE', 'Expense'

    # amount = models.DecimalField(max_digits=12, decimal_places=2)
    # FIX 1: MinValueValidator lagaya taaki 0 ya negative amount save na ho sake
    amount = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))] 
    )

    record_type = models.CharField(max_length=10, choices=RecordType.choices) 
    category = models.CharField(max_length=50, db_index=True)
    # date = models.DateField(db_index=True)
    date = models.DateField(
        db_index=True,
        validators=[validate_past_or_today]
    )
    
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