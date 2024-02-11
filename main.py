from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QListWidget, QScrollArea
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette, QColor, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QStyleFactory
import pyperclip
from urllib.parse import urlparse

class ClickSelectLineEdit(QLineEdit):
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.selectAll()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Amazon URL Processor")

        # Set the window size
        self.resize(450, 500)

        # Set the window icon
        self.setWindowIcon(QIcon('box-icon.png'))

        # Create the widgets
        self.url_label = QLabel("Amazon URL:")
        self.url_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #000000;")
        self.url_entry = ClickSelectLineEdit()
        self.url_entry.setStyleSheet("background-color: #FAF9F6;")
        self.url_entry.returnPressed.connect(self.process_url)

        # Create the buttons
        self.enter_url_button = QPushButton("Process URL")
        self.enter_url_button.setStyleSheet("background-color: #CD4F41; color: #000000; font-size: 16px; font-weight: bold;")
        self.enter_url_button.clicked.connect(self.process_url)

        self.clear_button = QPushButton("Clear all")
        self.clear_button.setStyleSheet("background-color: #CD4F41; color: #000000; font-size: 16px; font-weight: bold;")
        self.clear_button.clicked.connect(self.clear_all)

        self.product_name_label = QLabel("Product Name:")
        self.product_name_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #000000;")
        self.product_name_entry = ClickSelectLineEdit()
        self.product_name_entry.setStyleSheet("background-color: #FAF9F6;")

        self.product_id_label = QLabel("Product ID:")
        self.product_id_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #000000;")
        self.product_id_entry = ClickSelectLineEdit()
        self.product_id_entry.setStyleSheet("background-color: #FAF9F6;")

        # Create the listbox
        layout = QVBoxLayout()

        self.history_listbox = QListWidget()
        self.history_listbox.setStyleSheet("background-color: #FAF9F6;")

        layout.addWidget(self.url_label)
        layout.addWidget(self.url_entry)
        layout.addWidget(self.product_name_label)
        layout.addWidget(self.product_name_entry)
        layout.addWidget(self.product_id_label)
        layout.addWidget(self.product_id_entry)
        layout.addWidget(self.enter_url_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.history_listbox)
        
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # Create the status bar
        self.statusBar = self.statusBar()

    # Process the URL
    def process_url(self):
        # Get the URL from the entry
        url = self.url_entry.text()
        parsed_url = urlparse(url)

        # Check if the URL is valid from Amazon
        if parsed_url.netloc != "www.amazon.com":
            self.url_label.setText("Please enter a valid Amazon URL!")
            QTimer.singleShot(2000, lambda: self.url_label.setText("Amazon URL:"))
        else:
            self.url_label.setText("Amazon URL:")
            product_id = url.split("/dp/")[1].split("/")[0] if "/dp/" in url else ""
            product_name = url.split("/")[3].replace("-", " ") if len(url.split("/")) > 3 else ""
            pyperclip.copy(product_id)

            self.product_name_entry.setText(product_name)
            self.product_id_entry.setText(product_id)

            self.history_listbox.insertItem(0, url)

            self.statusBar.showMessage("Product ID has been copied to clipboard!", 3000)

            QTimer.singleShot(3000, self.statusBar.clearMessage)
        

    def clear_all(self):
        self.url_entry.clear()
        self.product_name_entry.clear()
        self.product_id_entry.clear()
        self.history_listbox.clear()

def set_theme(app):
    app.setStyle(QStyleFactory.create("Fusion"))
    palette = QPalette()

    palette.setColor(QPalette.Window, QColor(244, 217, 174))
    palette.setColor(QPalette.WindowText, QColor(28, 64, 76))
    palette.setColor(QPalette.Base, QColor(45, 128, 119))
    palette.setColor(QPalette.AlternateBase, QColor(244, 217, 174))
    palette.setColor(QPalette.ToolTipBase, QColor(28, 64, 76))
    palette.setColor(QPalette.ToolTipText, QColor(28, 64, 76))
    palette.setColor(QPalette.Text, QColor(28, 64, 76))
    palette.setColor(QPalette.Button, QColor(205, 79, 65))
    palette.setColor(QPalette.ButtonText, QColor(28, 64, 76))  # Set to same color as QPalette.Text
    palette.setColor(QPalette.BrightText, QColor(222, 158, 70))
    palette.setColor(QPalette.Link, QColor(45, 128, 119))
    palette.setColor(QPalette.Highlight, QColor(0, 0, 0))
    palette.setColor(QPalette.HighlightedText, QColor(250, 249, 246))

    app.setPalette(palette)

    app.setStyleSheet("""
    QToolTip { color: #1c404c; background-color: #f4d9ae; 
    border: 1px solid #000000; }
                      
    QWidget { font-size: 16px; 
    font-family: Arial; 
    font-weight: bold; }
                      
    ClickSelectLineEdit, QTextEdit { color: #000000; }
    QStatusBar { color: #000000; }
    """)

def main():
    app = QApplication([])
    set_theme(app)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()