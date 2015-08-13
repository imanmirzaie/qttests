# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 12:34:35 2014

@author: Seyed Iman Mirzaei
"""

import sys

from PySide.QtCore import *
from PySide.QtGui import *

def sayhello():
    print("Hello!")

app = QApplication(sys.argv)

button1 = QPushButton("Push button 1")
button1.clicked.connect(sayhello)
button1.show()

app.exec_()
