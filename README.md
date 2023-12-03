# Selenium_AZ_Price_Grab

**Overview**
Uses Selenium to grab prices from Amazon.

This simple Python program utilizes the Selenium library to scrape the price of a product on Amazon. It automates the process of opening a Chrome browser, navigating to a specific Amazon product page, and extracting the price information.

**Prerequisites**
Before running the script, make sure you have the following installed:
- Python (the code is written in Python 3)
- Selenium library
- ChromeDriver (ensure it matches your Chrome browser version)

**Usage**
- Replace the URL in the driver.get() method with the URL of the Amazon product you want to track.
- Run the script using the following command: python amazon_price_scraper.py

**Important Note**
Please be aware that web scraping may violate the terms of service of a website. Ensure that you have the right to scrape data from the target website, and use this script responsibly and ethically.

**Explanation of the Code**
The program uses Selenium to automate interactions with the Chrome browser.
It navigates to the specified Amazon product page.
It locates the price elements using their class names and extracts the dollar and cents components.
The final price is printed to the console.

**Additional Configuration**
The code includes an option to keep the Chrome browser open even after the program finishes. If this behavior is not desired, you can remove or modify the following lines:
- chrome_options = webdriver.ChromeOptions()
- chrome_options.add_experimental_option("detach", True)
- driver = webdriver.Chrome(options=chrome_options)

**Disclaimer**
This script should be used responsibly. Be aware of the legal and ethical implications of web scraping, and respect the terms of service of the websites you interact with.
