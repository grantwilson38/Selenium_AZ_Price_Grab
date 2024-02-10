from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QListWidget, QScrollArea
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette, QColor, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QStyleFactory
import pyperclip

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Amazon URL Extractor")

        # Set the window icon
        self.setWindowIcon(QIcon('C:\\Users\\grant\\python-projects\\selenium_amazon_price_grab\\icons8-new-product-96.png'))
        self.url_label = QLabel("Enter an Amazon URL and press enter:")
        self.url_entry = QLineEdit()
        self.url_entry.returnPressed.connect(self.enter_new_url)

        self.product_name_label = QLabel("Product Name:")
        self.product_name_entry = QLineEdit()

        self.product_id_label = QLabel("Product ID:")
        self.product_id_entry = QLineEdit()

        self.enter_url_button = QPushButton("Enter another URL")
        self.enter_url_button.clicked.connect(self.enter_new_url)

        self.history_listbox = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_entry)
        layout.addWidget(self.product_name_label)
        layout.addWidget(self.product_name_entry)
        layout.addWidget(self.product_id_label)
        layout.addWidget(self.product_id_entry)
        layout.addWidget(self.enter_url_button)
        layout.addWidget(self.history_listbox)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.statusBar = self.statusBar()

    def enter_new_url(self):
        url = self.url_entry.text()
        product_id = url.split("/dp/")[1].split("/")[0] if "/dp/" in url else ""
        product_name = url.split("/")[3].replace("-", " ") if len(url.split("/")) > 3 else ""
        pyperclip.copy(product_id)

        self.product_name_entry.setText(product_name)
        self.product_id_entry.setText(product_id)

        self.history_listbox.insertItem(0, url)

        self.statusBar.showMessage("Product ID has been copied to clipboard!", 3000)

        QTimer.singleShot(3000, self.statusBar.clearMessage)

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
    palette.setColor(QPalette.ButtonText, QColor(244, 217, 174))
    palette.setColor(QPalette.BrightText, QColor(222, 158, 70))
    palette.setColor(QPalette.Link, QColor(45, 128, 119))
    palette.setColor(QPalette.Highlight, QColor(45, 128, 119))
    palette.setColor(QPalette.HighlightedText, QColor(244, 217, 174))

    app.setPalette(palette)
    app.setStyleSheet("""
    QToolTip { color: #1c404c; background-color: #f4d9ae; border: 1px solid #cd4f41; }
    QWidget { font-size: 16px; font-family: Arial; font-weight: bold; }
    QLineEdit, QTextEdit { color: #f4d9ae; }
    """)

def main():
    app = QApplication([])
    set_theme(app)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()