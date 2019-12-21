import tkinter as tk
from tkinter import messagebox

# Define categories for expenses
expense_categories = ["Food", "Transportation", "Entertainment", "Bills", "Others"]

# Create the main application window
root = tk.Tk()
root.title("Expense Tracker")

# Function to handle saving expenses
def save_expense():
    # Placeholder function for now
    messagebox.showinfo("Save Expense", "Expense saved successfully.")

# Function to handle viewing expenses
def view_expenses():
    # Placeholder function for now
    messagebox.showinfo("View Expenses", "Here are your expenses.")

# Create labels and entry fields for each category
category_entries = {}
for category in expense_categories:
    label = tk.Label(root, text=category)
    label.pack()

    entry = tk.Entry(root, width=15)
    entry.pack()
    
    category_entries[category] = entry

# Create buttons for saving and viewing expenses
save_button = tk.Button(root, text="Save Expense", command=save_expense)
save_button.pack(pady=10)

view_button = tk.Button(root, text="View Expenses", command=view_expenses)
view_button.pack(pady=10)

# Run the main event loop
root.mainloop()

# Function to handle saving expenses
def save_expense():
    expenses = {}
    for category, entry in category_entries.items():
        value = entry.get()
        if value.isdigit():
            expenses[category] = float(value)
        else:
            messagebox.showerror("Error", f"Invalid value entered for {category}. Please enter a number.")
            return

    # You can save 'expenses' dictionary to a file or database here
    messagebox.showinfo("Save Expense", "Expenses saved successfully.")

# Function to handle viewing expenses
def view_expenses():
    expenses = ""
    for category, entry in category_entries.items():
        value = entry.get()
        if value:
            expenses += f"{category}: ${value}\n"
    
    if expenses:
        messagebox.showinfo("View Expenses", expenses.strip())
    else:
        messagebox.showwarning("No Expenses", "No expenses recorded yet.")
