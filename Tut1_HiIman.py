# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 11:32:23 2014

@author: Seyed Iman Mirzaei
"""

import sys
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication(sys.argv)
label = QLabel("Hi Iman! \nHow are you?!")
label.show()
app.exec_()
sys.exit()