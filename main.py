# Description: This program opens a Chrome browser and
# goes to Amazon to get the price of a product. It then
# asks the user for a code to bypass the captcha and
# finally displays the product ID and price in a dialog box.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Text, simpledialog, Tk, messagebox, Toplevel, Label, CENTER
import time
from selenium.common.exceptions import NoSuchElementException
import pyperclip

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create a dialog to ask for the URL
root = Tk()
root.withdraw()  # Hide the main window
url = simpledialog.askstring("URL Input", "Please enter the Amazon URL:")

# Open Chrome and go to Amazon
driver = webdriver.Chrome(options=chrome_options)
driver.get(url) 

# Wait for the code input field to be present
wait = WebDriverWait(driver, 10)
code_input = wait.until(EC.presence_of_element_located((By.ID, 'captchacharacters')))

# Ask the user for the code
code = simpledialog.askstring("Code Input", "Please enter the code:")

# Enter the code and submit the form
code_input.send_keys(code)
code_input.submit()

# Wait for the product page to load
wait.until(EC.element_to_be_clickable((By.ID, 'productTitle')))

# Get product id from url between /dp/ and /ref
product_id = driver.current_url.split("/dp/")[1].split("/")[0]
pyperclip.copy(product_id)  # Copy the product ID to the clipboard

# Get the price
try:
    price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole").text
    price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
except NoSuchElementException:
    price_dollar = "Not found"
    price_cents = ""

# Create a custom dialog box
dialog = Toplevel()
dialog.title("Product Information")
dialog.geometry("300x200")  # Set the size of the dialog box

# Center the dialog box
window_width = dialog.winfo_reqwidth()
window_height = dialog.winfo_reqheight()
position_right = int(dialog.winfo_screenwidth()/2 - window_width/2)
position_down = int(dialog.winfo_screenheight()/2 - window_height/2)
dialog.geometry("+{}+{}".format(position_right, position_down))

# Add a text widget with the product ID and price
text = Text(dialog)
text.insert('1.0', f"Product ID: {product_id}\nPrice: {price_dollar}.{price_cents}")
text.pack(padx=10, pady=10)  # Add padding around the text widget

dialog.mainloop()  # Keep the dialog box open

driver.quit()  # Close the browser