import os
import django
import random
from datetime import date, timedelta

# 1. Django Environment Setup (Taaki script database se baat kar sake)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_backend.settings')
django.setup()

from django.contrib.auth import get_user_model
from records.models import FinancialRecord

User = get_user_model()

def seed_database():
    print("🌱 Database seeding start ho rahi hai...")

    # Admin user dhoondhein (Jiske naam par records save honge)
    admin_user = User.objects.filter(is_superuser=True).first()
    if not admin_user:
        print("❌ Error: Koi admin nahi mila. Pehle 'python manage.py createsuperuser' run karein!")
        return

    # Realistic Dummy Data Categories
    incomes = [
        ("Monthly Salary", 85000), ("Freelance Project", 15000), 
        ("Stock Dividends", 4500), ("Diwali Bonus", 12000)
    ]
    expenses = [
        ("House Rent", 18000), ("Groceries", 7500), ("Electricity Bill", 2200),
        ("Wifi & Mobile", 1500), ("Swiggy/Zomato", 3000), ("Bike Petrol", 3500), 
        ("Gym Membership", 1200), ("Netflix Subscription", 649)
    ]

    records_to_create = []
    today = date.today()

    # Pichle 30 din ka data generate karte hain (Total 20 records)
    for _ in range(20):
        is_income = random.choice([True, False, False]) # Kharcha zyada baar select hoga (Reality!)
        random_date = today - timedelta(days=random.randint(0, 30))

        if is_income:
            category, amount = random.choice(incomes)
            record_type = 'INCOME'
        else:
            category, amount = random.choice(expenses)
            record_type = 'EXPENSE'

        records_to_create.append(
            FinancialRecord(
                amount=amount,
                record_type=record_type,
                category=category,
                date=random_date,
                notes=f"Auto-generated dummy record for {category}",
                created_by=admin_user
            )
        )

    # Database mein ek saath save karein (Fast insertion)
    FinancialRecord.objects.bulk_create(records_to_create)
    print(f"✅ SUCCESS: {len(records_to_create)} dummy records database mein add ho gaye hain!")

if __name__ == '__main__':
    # Purana data clean karna ho toh (Optional, abhi comment kiya hai)
    # FinancialRecord.objects.all().delete() 
    seed_database()