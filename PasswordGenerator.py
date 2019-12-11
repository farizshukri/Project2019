import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Function to generate a password
def generate_password():
    length = int(length_entry.get())

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than zero.")
        return

    # Define the character sets to generate passwords from
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine all character sets
    all_chars = lowercase_letters + uppercase_letters + digits + punctuation

    # Generate password
    password = ''.join(random.sample(all_chars, length))
    
    # Update password display
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create labels and entry fields
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

length_entry = tk.Entry(root, width=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

password_entry = tk.Entry(root, width=30, state='readonly')
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Run the main event loop
root.mainloop()
