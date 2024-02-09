from tkinter import Tk, Label, Entry, Toplevel, simpledialog, Button, Listbox, Scrollbar
import pyperclip

class CustomDialog(simpledialog.Dialog):
    def body(self, master):
        self.title("URL Input")
        Label(master, text="Please enter the Amazon URL:").grid(row=0)
        self.e1 = Entry(master, width=100)
        self.e1.grid(row=0, column=1)
        return self.e1 # initial focus

    def apply(self):
        url = self.e1.get()
        product_id = url.split("/dp/")[1].split("/")[0] if "/dp/" in url else ""
        product_name = url.split("amazon.com/")[1].split("/dp")[0].replace("-", " ") if "amazon.com/" in url and "/dp" in url else ""
        pyperclip.copy(product_id)  # Copy the product ID to the clipboard

        # Add the URL to the history listbox
        history_listbox.insert(0, url)

        # Create a new window with a blue background
        new_window = Toplevel(root, bg='light blue')
        new_window.title("URL and Product ID")

        # Create an Entry widget displaying the URL with a larger, bold font
        url_label = Label(new_window, text="URL:", font=("Arial", 18, "bold"), bg='light blue')
        url_label.pack(padx=20, pady=20)  # Add more padding
        url_entry = Entry(new_window, width=100, font=("Arial", 18))
        url_entry.insert(0, url)  # Insert the URL into the Entry widget
        url_entry.pack(padx=20, pady=20)  # Add more padding
        url_entry.bind('<ButtonRelease-1>', self.select_all)  # Bind the select_all function to the left mouse button release event

        # Create an Entry widget for the product name with a larger, bold font
        product_name_label = Label(new_window, text="Product Name:", font=("Arial", 18, "bold"), bg='light blue')
        product_name_label.pack(padx=20, pady=20)  # Add more padding
        product_name_entry = Entry(new_window, width=100, font=("Arial", 18))  # Set the width to 100
        product_name_entry.insert(0, product_name)  # Insert the product name into the Entry widget
        product_name_entry.pack(padx=20, pady=20)  # Add more padding
        product_name_entry.bind('<ButtonRelease-1>', self.select_all)  # Bind the select_all function to the left mouse button release event

        # Create an Entry widget displaying the product ID with a larger, bold font
        product_id_label = Label(new_window, text="Product ID:", font=("Arial", 18, "bold"), bg='light blue')
        product_id_label.pack(padx=20, pady=20)  # Add more padding
        product_id_entry = Entry(new_window, width=100, font=("Arial", 18))
        product_id_entry.insert(0, product_id)  # Insert the product ID into the Entry widget
        product_id_entry.pack(padx=20, pady=20)  # Add more padding
        product_id_entry.bind('<ButtonRelease-1>', self.select_all)  # Bind the select_all function to the left mouse button release event

        # Create a button for entering another URL with a larger, bold font
        enter_url_button = Button(new_window, text="Enter another URL", command=self.enter_new_url, font=("Arial", 18, "bold"))
        enter_url_button.pack(padx=20, pady=20)  # Add more padding

    def enter_new_url(self):
        # Open the custom dialog for entering another URL
        d = CustomDialog(root)

    def select_all(self, event):
        # Select all the text in the Entry widget
        event.widget.select_range(0, 'end')
        event.widget.focus()

root = Tk()

# Create a listbox for the history of URLs
history_listbox = Listbox(root)
history_listbox.pack(side="right", fill="both", expand=True)

# Add a scrollbar to the listbox
scrollbar = Scrollbar(history_listbox)
scrollbar.pack(side="right", fill="y")

# Attach the scrollbar to the listbox
history_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=history_listbox.yview)

d = CustomDialog(root)
root.mainloop()  # Start the main event loop