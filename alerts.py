# Check for alerts based on high usage, high bill amount, or voltage fluctuations
def check_alerts(units, bill_amount):
    alerts = []
    
    if units > 1200:
        alerts.append("⚠ High Consumption Alert: Your electricity usage is unusually high!")
    
    if bill_amount > 8000:
        alerts.append("⚠ High Bill Alert: Your bill amount is significantly high. Consider reducing usage.")
    
    # Simulated voltage fluctuation detection
    import random
    voltage = random.randint(180, 260)  # Simulating voltage readings
    
    if voltage > 240:
        alerts.append(f"⚠ High Voltage Alert: Detected {voltage}V! Risk of appliance damage.")
    elif voltage < 190:
        alerts.append(f"⚠ Low Voltage Alert: Detected {voltage}V! Possible appliance malfunction.")
    
    return alerts
