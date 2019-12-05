import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button

# Create the main application window
root = tk.Tk()
root.title("Chatbot")

# Create a text display area
text_area = Text(root, height=20, width=50, font=("Arial", 12))

# Create a scrollbar for the text area
scrollbar = Scrollbar(root, command=text_area.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
text_area.config(yscrollcommand=scrollbar.set)

# Function to handle sending messages
def send_message(event=None):
    message = entry_field.get()
    if message.strip() == "":
        return
    
    # Display user message in the text area
    text_area.insert(tk.END, "You: " + message + "\n")
    text_area.see(tk.END)  # Scroll to the bottom
    
    # Placeholder for generating bot response
    bot_response = "Bot: Hello! How can I assist you?"
    
    # Display bot response in the text area
    text_area.insert(tk.END, bot_response + "\n")
    text_area.see(tk.END)  # Scroll to the bottom
    
    # Clear the entry field after sending message
    entry_field.delete(0, tk.END)

# Create an entry field for typing messages
entry_field = Entry(root, width=50)
entry_field.bind("<Return>", send_message)  # Bind Enter key to send message
entry_field.pack(pady=10)

# Create a send button
send_button = Button(root, text="Send", command=send_message)
send_button.pack()

# Run the main event loop
root.mainloop()
