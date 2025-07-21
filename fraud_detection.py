from data_handler import load_user_data

def detect_fraud(user_id, units):
    past_data = load_user_data(user_id)
    
    if not past_data:
        return None  # No past data available
    
    # Convert all values in past_data to float
    past_data = [float(value) for value in past_data if value.replace('.', '', 1).isdigit()]
    
    if not past_data:  
        return None  # No valid numeric data
    
    avg_usage = sum(past_data) / len(past_data)
    
    if units > 2 * avg_usage:
        return "Fraud Alert: Unusual high usage detected!"

    return None