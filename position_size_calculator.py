import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        entry_price = float(entry_price_entry.get())
        stop_loss = float(stop_loss_entry.get())
        risk_amount = float(risk_amount_entry.get())
        
        # Determine if position is long or short
        if position_type.get() == "Long":
            risk_per_share = entry_price - stop_loss
            if risk_per_share <= 0:
                messagebox.showerror("Input Error", "For a long position, entry price must be greater than stop loss price!")
                return
        else:  # Short position
            risk_per_share = stop_loss - entry_price
            if risk_per_share <= 0:
                messagebox.showerror("Input Error", "For a short position, stop loss price must be greater than entry price!")
                return
        
        num_shares = risk_amount / risk_per_share
        result_label.config(text=f"Position Size: {num_shares:.2f} shares")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Stock Position Size Calculator")

# Position Type (Long/Short) toggle using radio buttons
position_type = tk.StringVar(value="Long")
tk.Label(root, text="Position Type:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
long_radio = tk.Radiobutton(root, text="Long", variable=position_type, value="Long")
long_radio.grid(row=0, column=1, padx=10, pady=10, sticky="w")
short_radio = tk.Radiobutton(root, text="Short", variable=position_type, value="Short")
short_radio.grid(row=0, column=2, padx=10, pady=10, sticky="w")

# Entry Price input
tk.Label(root, text="Entry Price:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_price_entry = tk.Entry(root)
entry_price_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

# Stop Loss Price input
tk.Label(root, text="Stop Loss Price:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
stop_loss_entry = tk.Entry(root)
stop_loss_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

# Riskable Amount input
tk.Label(root, text="Riskable Amount:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
risk_amount_entry = tk.Entry(root)
risk_amount_entry.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=0, columnspan=3, pady=10)

# Result Label
result_label = tk.Label(root, text="Position Size: ")
result_label.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
