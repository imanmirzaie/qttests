# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 11:38:54 2014

@author: Seyed Iman Mirzaei
"""

import sys

import PySide
from PySide.QtGui import QApplication
from PySide.QtGui import QMessageBox

app = QApplication(sys.argv)

msgbox = QMessageBox()
msgbox.setText("Hey! you are using PySide version " + PySide.__version__)
msgbox.exec_()