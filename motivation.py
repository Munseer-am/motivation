#! /usr/bin/env python
import random
# import requests
import sys
from quotes import quotes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Motivational Quotes")
        label = QLabel(self)
        pixmap = QPixmap('cat.jpg')
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

# try:
    # request = requests.get("https://google.com/", timeout=5)
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
# except (requests.ConnectionError, requests.Timeout) as e:
    # print("check your internet connection")
