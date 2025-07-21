import random
from datetime import datetime

# Simulate unit consumption (random values for testing)
def generate_units():
    return random.randint(10, 1500)

# Calculate bill based on units consumed
def calculate_bill(units):
    if units < 500:
        if units <= 100:
            bill_amount = 0
        elif units <= 200:
            bill_amount = units * 2.35
        elif units <= 400:
            bill_amount = units * 4.70
        else:  # 401 to 500
            bill_amount = units * 6.30
    else:
        if units <= 400:
            bill_amount = units * 4.70
        elif units <= 500:
            bill_amount = units * 6.30
        elif units <= 600:
            bill_amount = units * 8.40
        elif units <= 800:
            bill_amount = units * 9.45
        elif units <= 1000:
            bill_amount = units * 10.50
        else:
            bill_amount = units * 11.55

    # Apply late fee if past due date
    today = datetime.now().day
    late_fee = 50 if today > 10 else 0
    bill_amount += late_fee

    return bill_amount, late_fee
