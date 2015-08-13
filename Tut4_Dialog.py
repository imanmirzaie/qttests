# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 13:44:53 2014

@author: Seyed Iman Mirzaei
"""

import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.setWindowTitle("My Form")
        # Create widgets
        self.edit = QLineEdit("Write my name here..")
        self.button1 = QPushButton("Show Greetings")
        self.button2 = QPushButton('EXIT')
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button1.clicked.connect(self.greetings)
        # setup exit button
        self.button2.clicked.connect(exit)
        
    # Greets the user
    def greetings(self):
        print ("Hello %s" % self.edit.text())
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())