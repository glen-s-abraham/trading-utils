import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd

def calculate_rebalance():
    try:
        num_equities = int(entry_num_equities.get())
        
        equities = []
        
        total_market_value = 0
        for i in range(num_equities):
            name = entries[i]["name"].get()
            quantity = int(entries[i]["quantity"].get())
            avg_price = float(entries[i]["avg_price"].get())
            current_price = float(entries[i]["current_price"].get())
            allocation = float(entries[i]["allocation"].get())
            
            market_value = quantity * current_price
            total_market_value += market_value
            
            equities.append({
                "Name": name,
                "Current Quantity": quantity,
                "Average Price": avg_price,
                "Current Price": current_price,
                "Allocation %": allocation,
                "Market Value": market_value
            })
        
        df = pd.DataFrame(equities)
        df["Target Value"] = (df["Allocation %"] / 100) * total_market_value
        df["Difference"] = df["Target Value"] - df["Market Value"]
        df["Buy/Sell Quantity"] = df["Difference"] / df["Current Price"]
        
        # Clear the previous table
        for row in tree.get_children():
            tree.delete(row)
        
        for _, row in df.iterrows():
            tree.insert("", "end", values=list(row))
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def create_equity_fields():
    try:
        num_equities = int(entry_num_equities.get())
        for widget in frame_equities.winfo_children():
            widget.destroy()
        
        global entries
        entries = []
        
        header_labels = ["Equity", "Name", "Current Quantity", "Average Price", "Current Price", "Allocation %"]
        for col, text in enumerate(header_labels):
            tk.Label(frame_equities, text=text, width=15, anchor="w", relief="ridge").grid(row=0, column=col, padx=5, pady=5, sticky="ew")
        
        for i in range(num_equities):
            tk.Label(frame_equities, text=f"Equity {i+1}:", width=15, anchor="w", relief="ridge").grid(row=i+1, column=0, padx=5, pady=2, sticky="ew")
            name = tk.Entry(frame_equities, width=15)
            name.grid(row=i+1, column=1, padx=5)
            quantity = tk.Entry(frame_equities, width=15)
            quantity.grid(row=i+1, column=2, padx=5)
            avg_price = tk.Entry(frame_equities, width=15)
            avg_price.grid(row=i+1, column=3, padx=5)
            current_price = tk.Entry(frame_equities, width=15)
            current_price.grid(row=i+1, column=4, padx=5)
            allocation = tk.Entry(frame_equities, width=15)
            allocation.grid(row=i+1, column=5, padx=5)
            
            entries.append({"name": name, "quantity": quantity, "avg_price": avg_price, "current_price": current_price, "allocation": allocation})
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of equities.")

root = tk.Tk()
root.title("Portfolio Rebalancer")
root.geometry("850x500")

tk.Label(root, text="Number of Equities:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_num_equities = tk.Entry(root, width=10)
entry_num_equities.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Set Fields", command=create_equity_fields).grid(row=0, column=2, padx=5, pady=5)

frame_equities = tk.Frame(root)
frame_equities.grid(row=1, column=0, columnspan=6, padx=5, pady=5)

tk.Button(root, text="Rebalance Portfolio", command=calculate_rebalance).grid(row=2, column=0, columnspan=2, pady=10, padx=5)

columns = ["Name", "Current Quantity", "Average Price", "Current Price", "Allocation %", "Market Value", "Target Value", "Difference", "Buy/Sell Quantity"]
tree = ttk.Treeview(root, columns=columns, show="headings", height=5)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")

tree.grid(row=3, column=0, columnspan=6, padx=5, pady=5, sticky="ew")

root.mainloop()
