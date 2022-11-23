#! /usr/bin/env python
import random
import requests
import sys
from quotes import quotes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Motivational Quotes")
        pixmap = QPixmap()
        pixmap.loadFromData(requests.get("https://munseer.pythonanywhere.com/static/logo.jpg").content)
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
