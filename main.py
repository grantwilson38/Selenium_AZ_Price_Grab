import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Text, simpledialog, Tk, messagebox, Toplevel, Label, CENTER, font, Entry, StringVar
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pyperclip

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Disable the logging
caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'OFF'}

# Create a dialog to ask for the URL
root = Tk()
root.withdraw()  # Hide the main window
url = simpledialog.askstring("URL Input", "Please enter the Amazon URL:")

# Open Chrome and go to Amazon
driver = webdriver.Chrome(options=chrome_options)
driver.get(url) 

def on_input(evt):
    # Function to be called whenever the user types something
    content = captcha_code.get()
    if len(content) == 6:  # If the user has typed in six characters
        root.withdraw()  # Hide the main window
        time.sleep(1)  # Wait for the window to be hidden

try:
    # Wait for the code input field to be present
    wait = WebDriverWait(driver, 10)
    try:
        code_input = wait.until(EC.presence_of_element_located((By.ID, 'captchacharacters')))

        # Ask the user for the code
        root.deiconify()  # Show the main window
        root.title("Code Input")
        root.attributes('-topmost', 1)  # Keep the window on top
        Label(root, text="Please enter the captcha:").pack()
        captcha_code = StringVar()
        captcha_entry = Entry(root, textvariable=captcha_code, font=("Helvetica", 16))
        captcha_entry.pack()
        captcha_entry.bind('<KeyRelease>', on_input)
        root.mainloop()

        # After the window is destroyed, you can still access the captcha code
        print("Captcha code:", captcha_code.get())

        # Enter the code
        code = captcha_code.get()
        code_input.send_keys(code)

        # Find the submit button and click it
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and @class='a-button-text' and text()='Continue shopping']")))
        submit_button.click()
    except TimeoutException:
        # Captcha did not appear, do nothing
        pass

    # Wait for the product page to load
    wait.until(EC.element_to_be_clickable((By.ID, 'productTitle')))

    # Get product id from url between /dp/ and /ref
    product_id = driver.current_url.split("/dp/")[1].split("/")[0]
    pyperclip.copy(product_id)  # Copy the product ID to the clipboard

    # Make the main window visible again
    root.deiconify()

    # Create a custom dialog box
    dialog = Toplevel(root)
    dialog.title("Product Information")
    dialog.geometry("400x300")  # Set the size of the dialog box

    # Center the dialog box
    window_width = dialog.winfo_reqwidth()
    window_height = dialog.winfo_reqheight()
    position_right = int(dialog.winfo_screenwidth()/2 - window_width/2)
    position_down = int(dialog.winfo_screenheight()/2 - window_height/2)
    dialog.geometry("+{}+{}".format(position_right, position_down))

    # Add a text widget with the product ID
    text = Text(dialog, font=("Helvetica", 16), padx=20, pady=20)
    text.insert('1.0', f"Product ID: {product_id}")
    text.pack(padx=20, pady=20)  # Add padding around the text widget

    dialog.mainloop()  # Keep the dialog box open
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()  # Close the browser