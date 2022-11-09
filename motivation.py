#! /usr/bin/env python
import random
import sys
from quotes import quotes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Motivation Quotes")
        self.setWindowIcon(QIcon('1250593.png'))
        r = random.choice(quotes).upper()
        # quotes.remove(r)
        self.widget = QLabel("“" + "".join(r) + "”".upper())
        # widget = QLabel(quotes[0])
        font = self.widget.font()
        font.setPointSize(30)
        self.widget.setFont(font)
        self.widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.widget)
        self.setFixedHeight(500)
        self.setFixedWidth(650)
        self.widget.adjustSize()
        self.widget.setWordWrap(True)
        self.update_timer = QTimer()
        # self.update_timer.setInterval(20)
        self.update_timer.setSingleShot(False)
        self.update_timer.start(10000)
        self.update_timer.timeout.connect(self.update)

    def update(self):
        try:
            r = random.choice(quotes)
            quotes.remove(r)
            s = "“" + "".join(r) + "”"
            self.widget.setText(s.upper())
        except Exception as e:
            sys.exit()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
