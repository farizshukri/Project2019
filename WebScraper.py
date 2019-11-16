import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup

# Create the main application window
root = tk.Tk()
root.title("Web Scraper")

# Function to handle scraping
def scrape_website():
    url = url_entry.get().strip()
    
    if not url:
        messagebox.showwarning("Warning", "Please enter a URL.")
        return
    
    try:
        # Send HTTP request and get the content
        response = requests.get(url)
        response.raise_for_status()  # Raise error for invalid HTTP response
    
        # Parse HTML using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract data here (e.g., save to a file)
        filename = save_data(soup)
        
        messagebox.showinfo("Success", f"Data scraped successfully and saved to {filename}")
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching URL: {e}")
    
# Function to save data extracted from webpage
def save_data(soup):
    # Example: Extract all text from the webpage and save to a text file
    text_data = soup.get_text()
    filename = 'web_data.txt'
    
    # Ask user to select a folder to save the file
    save_folder = filedialog.askdirectory()
    if save_folder:
        filepath = save_folder + '/' + filename
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(text_data)
        
    return filename

# Create labels, entry field, and buttons
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

scrape_button = tk.Button(root, text="Scrape Website", command=scrape_website)
scrape_button.pack(pady=10)

# Run the main event loop
root.mainloop()
