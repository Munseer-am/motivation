#! /usr/bin/env python
import random
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

quotes = [
    "First forget inspiration. Habit is more dependable. Habit will sustain you whether you're inspired or not. Habit will help you finish and polish your stories. Inspiration won't. Habit is persistence in practice.",
    "Keep your friends rich, but your enemies richer", 
    "Life begins at the end your comfort zone", 
    "Don't be same, be better!", 
    "All our dreams can come true, if we have the courage to pursue them.", 
    "success is not final;failure is not fatal; it is the courage to continue that counts",
    "SUCCESS comes to those who ACT",
    "Don't Focus On The Pain, Focus On the Progress",
    "If your dream don't scare you they are too small",
    "Think Big. Trust Yourself And Make It Happen",
    "A negative mind will never give you a positive life",
    "study hard play hard and be smart",
    "focus on the outcome not the obstacle"
    "you need to know what to do when the sun is not shining - RDJ",
    "just because you hit bottom, it doesn't mean that you have to stay there - RDJ",
    "You only fail when you stop trying",
    "good thing take time",
    "a smooth sea never made a skiller sailor",
    "the best fighter is never angry",
    "understand the results of your action",
    "train your mind to stay calm in every situation",
    "some enemies look like friends",
    "focus on the goals not the distractions",
    "success is not always what we see",
    "if there is no way create one",
    "happiness comes in wave it will find you again",
    "it nice to be important, but its important to be nice",
    ]

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("ini alppam motivation aakam")
        self.setWindowIcon(QIcon('1250593.png'))
        r = random.choice(quotes).upper()
        # quotes.remove(r)
        self.widget = QLabel("“"+"".join(r)+"”".upper())
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
        r = random.choice(quotes)
        quotes.remove(r)
        s = "“"+"".join(r)+"”"
        self.widget.setText(s.upper())

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

