import random
import uuid
from datetime import datetime, timedelta
from faker import Faker

def get_sales_data(language, num_rows):
    """
    Generates a list of dictionaries containing synthetic sales transactions.
    """
    # Set the start date for sales (e.g., 1 year ago)
    start_date = datetime.now() - timedelta(days=365)
    
    # 1. Localization Dictionaries & Faker Initialization
    if language == 'es':
        fake = Faker('es_CL')
        categories = ["Electronica", "Ropa", "Hogar", "Deportes", "Alimentos"]
        payment_methods = ["Tarjeta de Credito", "Efectivo", "Transferencia", "Debito"]
    else:
        fake = Faker('en_US')
        categories = ["Electronics", "Clothing", "Home", "Sports", "Groceries"]
        payment_methods = ["Credit Card", "Cash", "Bank Transfer", "Debit"]

    # 2. Data Generation
    rows = []
    
    for _ in range(num_rows):
        # Generate a random date and time within the last year
        random_days = random.randint(0, 365)
        transaction_date = start_date + timedelta(days=random_days, hours=random.randint(8, 20), minutes=random.randint(0, 59))
        
        # Base price for the transaction
        amount = round(random.uniform(15.0, 1500.0), 2) if language == 'en' else random.randint(15000, 1500000)

        record = {
            "transaction_id": f"TXN-{str(uuid.uuid4())[:8].upper()}",
            "customer_id": f"CUST-{random.randint(1000, 9999)}",
            "transaction_date": transaction_date.strftime("%Y-%m-%d %H:%M:%S"),
            "product_category": random.choice(categories),
            "payment_method": random.choice(payment_methods),
            "amount": amount,
            "currency": "CLP" if language == 'es' else "USD"
        }
        rows.append(record)
        
    return rows