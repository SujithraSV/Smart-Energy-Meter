import json
import os

DATA_FILE = "user_data.json"

# Load user data from file (or create an empty file if missing)
def load_user_data(user_id):
    if not os.path.exists(DATA_FILE):
        return {"units": 0, "bill_amount": 0, "prev_units": 0, "prev_bill": 0}
    
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
    
    return data.get(user_id, {"units": 0, "bill_amount": 0, "prev_units": 0, "prev_bill": 0})

# Save user data, keeping previous month's records
def save_data(user_id, units, bill_amount, late_fee):
    data = {}

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

    # Save previous month's data before overwriting
    prev_data = data.get(user_id, {"units": 0, "bill_amount": 0})
    
    data[user_id] = {
        "prev_units": prev_data["units"],
        "prev_bill": prev_data["bill_amount"],
        "units": units,
        "bill_amount": bill_amount,
        "late_fee": late_fee
    }

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

