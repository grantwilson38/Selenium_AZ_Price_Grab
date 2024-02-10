Amazon URL Extractor - README.md

Overview:

This Python application, Amazon URL Extractor, simplifies the process of retrieving product information from Amazon URLs. It leverages Qt5 for a user-friendly graphical interface (GUI) and provides the following functionalities:

Extract Product ID Automatically: Enter an Amazon product URL, and the tool automatically extracts and displays the relevant product ID.
Display Product Name: The app attempts to determine the product name based on the URL information, offering a user-friendly way to confirm its accuracy.
Copy Product ID to Clipboard: With a single click, copy the extracted product ID to your clipboard for convenient use in other applications.
Maintain URL History: View and manage a list of previously entered URLs in a convenient scroll area.
Customizable Theme: Apply different themes to personalize the look and feel of the interface.
Requirements:

Python 3.x
PyQt5 library (pip install PyQt5)
Optional: pyperclip library for advanced clipboard operations (pip install pyperclip)
Installation:

Clone or download the repository containing the Python script (main.py).
Install the required libraries: pip install PyQt5 [pyperclip] (optional).
Usage:

Run the application by executing python main.py in the terminal.
Enter an Amazon product URL in the designated field.
Press Enter or click the "Enter another URL" button.
The extracted product ID will be displayed and automatically copied to your clipboard.
The URL will be added to the history list for later reference.
Customization:

The application supports themes that adjust the UI's background and text colors. You can modify the color values in the set_theme function within the script to create your own themes.

Additional Notes:

The product name extraction is based on heuristics and may not always be accurate, especially for URLs with non-standard structures.
The functionality can be further expanded to include features like price scraping, review analysis, or integration with online price trackers.
