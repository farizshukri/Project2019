import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Text Adventure Game")

# Text area to display game output
output_text = tk.Text(root, height=20, width=50)
output_text.pack(padx=10, pady=10)

# Entry field for player input
entry_field = tk.Entry(root, width=50)
entry_field.pack(padx=10, pady=(0, 10))

# Function to handle player input
def process_command():
    command = entry_field.get().strip().lower()
    entry_field.delete(0, tk.END)  # Clear the entry field after getting input
    
    # Placeholder for game logic based on player input
    if command == "go north":
        output_text.insert(tk.END, "You go north.\n")
    elif command == "go south":
        output_text.insert(tk.END, "You go south.\n")
    else:
        output_text.insert(tk.END, "Invalid command. Try 'go north' or 'go south'.\n")
        
    # Scroll to the end of the text area
    output_text.see(tk.END)

# Button to submit player command
submit_button = tk.Button(root, text="Submit", command=process_command)
submit_button.pack()

# Run the main event loop
root.mainloop()
