import tkinter as tk
from tkinter import messagebox
import billing
import data_handler
import alerts
import fraud_detection
import matplotlib.pyplot as plt

# 🎯 Generate and Display Bill
def generate_bill():
    user_id = entry_user.get().strip()
    if not user_id:
        messagebox.showerror("Error", "Please enter a valid User ID")
        return

    prev_data = data_handler.load_user_data(user_id)
    prev_units = prev_data.get("units", 0)
    prev_bill = prev_data.get("bill_amount", 0)

    units = billing.generate_units()
    bill_amount, late_fee = billing.calculate_bill(units)

    data_handler.save_data(user_id, units, bill_amount, late_fee)

    alert_messages = alerts.check_alerts(units, bill_amount)
    fraud_alert = fraud_detection.detect_fraud(user_id, units)

    if fraud_alert:
        alert_messages.append(fraud_alert)
        fraud_detection.report_fraud(user_id, units, fraud_alert)

    result_text.set(f"🔹 Units: {units} kWh\n🔹 Bill: ₹{bill_amount}\n🔹 Late Fee: ₹{late_fee if late_fee else '0'}")

    if alert_messages:
        messagebox.showwarning("Alerts", "\n".join(alert_messages))

# 📊 Show Graph for Units and Cost Comparison
def show_graph():
    user_id = entry_user.get().strip()
    if not user_id:
        messagebox.showerror("Error", "Please enter a valid User ID")
        return

    user_data = data_handler.load_user_data(user_id)
    if user_data["units"] == 0:
        messagebox.showerror("Error", "No previous data found for this user")
        return

    prev_units = user_data.get("prev_units", 0)
    curr_units = user_data["units"]
    prev_cost = user_data.get("prev_bill", 0)
    curr_cost = user_data["bill_amount"]

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    ax[0].bar(["Previous Month", "Current Month"], [prev_units, curr_units], color=['blue', 'orange'])
    ax[0].set_xlabel("Month")
    ax[0].set_ylabel("Units Consumed (kWh)")
    ax[0].set_title("Electricity Usage Trend")

    ax[1].bar(["Previous Month", "Current Month"], [prev_cost, curr_cost], color=['green', 'red'])
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Bill Amount (₹)")
    ax[1].set_title("Bill Amount Trend")

    plt.tight_layout()
    plt.show()

# 💳 Payment Function
def pay_bill():
    messagebox.showinfo("Payment", "✅ Payment Successful!")

# 🎨 GUI Setup
root = tk.Tk()
root.title("Electricity Bill Management")
root.geometry("400x250")

tk.Label(root, text="Enter User ID:").grid(row=0, column=0, padx=10, pady=5)
entry_user = tk.Entry(root)
entry_user.grid(row=0, column=1, padx=10, pady=5)

btn_generate = tk.Button(root, text="Generate Bill", command=generate_bill)
btn_generate.grid(row=1, column=0, columnspan=2, pady=5)

btn_graph = tk.Button(root, text="View Usage & Cost Graph", command=show_graph)
btn_graph.grid(row=2, column=0, columnspan=2, pady=5)

btn_pay = tk.Button(root, text="Pay Bill", command=pay_bill)
btn_pay.grid(row=3, column=0, columnspan=2, pady=5)

result_text = tk.StringVar()
lbl_result = tk.Label(root, textvariable=result_text, font=("Arial", 12), fg="green")
lbl_result.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
