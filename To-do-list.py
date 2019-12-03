import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a task from the list
def remove_task():
    try:
        index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create labels, entry field, listbox, and buttons
task_label = tk.Label(root, text="Task:")
task_label.pack(pady=(10, 0))

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=(0, 10))

tasks_listbox = tk.Listbox(root, height=10, width=50)
tasks_listbox.pack()

add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", width=20, command=remove_task)
remove_button.pack(pady=5)

# Run the main event loop
root.mainloop()
