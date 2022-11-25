#! /usr/bin/env python
import random
import requests
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Motivational Quotes")
        pixmap2 = QPixmap()
        pixmap2.loadFromData(requests.get("https://munseer.pythonanywhere.com/static/logo.jpg").content)
        icon = QIcon(pixmap2)
        self.setMaximumHeight(768)
        self.setMaximumWidth(680)
        self.setWindowIcon(icon)
        self.set_image()
        self.reload = QShortcut(QKeySequence('Ctrl+R'), self)
        self.reload.activated.connect(self.set_image)
        self.quitSc = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.quitSc.activated.connect(QApplication.instance().quit)

    def set_image(self):
        self.label = QLabel(self)
        self.r = requests.get("https://munseer.pythonanywhere.com/quotes/")
        self.setCentralWidget(self.label)
        self.label.setMinimumSize(1, 1)
        pixmap1 = QPixmap()
        pixmap1.loadFromData(self.r.content)
        self.pixmap = pixmap1.scaled(self.width(), self.height())
        self.label.setPixmap(self.pixmap)
        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())
        self.label.resize(self.width(), self.height())

        

try:
    request = requests.get("https://google.com/", timeout=5)
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
except (requests.ConnectionError, requests.Timeout) as e:
    print("check your internet connection")
