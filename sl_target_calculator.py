import tkinter as tk
from tkinter import messagebox

class PositionCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Intraday Position Calculator")
        self.root.geometry("450x400")

        # Labels and Inputs
        tk.Label(root, text="Entry Price:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(root, text="Riskable Amount:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Label(root, text="Target-to-Risk Ratio:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        tk.Label(root, text="Entry Type (Long/Short):").grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.entry_price_input = tk.Entry(root)
        self.quantity_input = tk.Entry(root)
        self.riskable_amount_input = tk.Entry(root)
        self.ratio_input = tk.Entry(root)

        self.entry_price_input.grid(row=0, column=1, padx=10, pady=10)
        self.quantity_input.grid(row=1, column=1, padx=10, pady=10)
        self.riskable_amount_input.grid(row=2, column=1, padx=10, pady=10)
        self.ratio_input.grid(row=3, column=1, padx=10, pady=10)

        # Dropdown for Entry Type
        self.entry_type_var = tk.StringVar(value="Long")
        tk.OptionMenu(root, self.entry_type_var, "Long", "Short").grid(row=4, column=1, padx=10, pady=10)

        # Buttons
        calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        calculate_button.grid(row=5, column=0, columnspan=2, pady=20)

        # Result Labels
        self.result_label = tk.Label(root, text="", fg="blue", justify="left")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def calculate(self):
        try:
            # Get input values
            entry_price = float(self.entry_price_input.get())
            quantity = int(self.quantity_input.get())
            riskable_amount = float(self.riskable_amount_input.get())
            ratio = float(self.ratio_input.get() or 2)  # Default to 2 if not entered
            entry_type = self.entry_type_var.get()

            # Perform calculations
            risk_per_unit = riskable_amount / quantity

            if entry_type == "Long":
                stop_loss = entry_price - risk_per_unit
                target_price = entry_price + (ratio * risk_per_unit)
            elif entry_type == "Short":
                stop_loss = entry_price + risk_per_unit
                target_price = entry_price - (ratio * risk_per_unit)
            else:
                raise ValueError("Invalid entry type")

            # Display results
            result_text = (
                f"Entry Type: {entry_type}\n"
                f"Stop Loss: {stop_loss:.2f}\n"
                f"Target Price: {target_price:.2f}\n"
                f"Risk per Unit: {risk_per_unit:.2f}"
            )
            self.result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for all fields.")

# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = PositionCalculatorApp(root)
    root.mainloop()
