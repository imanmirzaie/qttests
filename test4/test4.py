# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test4.ui'
#
# Created: Tue Aug  5 15:32:35 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
x = np.linspace(-100,100,500)
y = np.sin(x)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

##################################################      
class MatplotlibWidget(Canvas):        
    def __init__(self, parent=None, title='Title', xlabel='x label', ylabel='y label', dpi=100, hold=False):
        super(MatplotlibWidget, self).__init__(Figure())

        self.setParent(parent)
        self.figure = Figure(dpi=dpi)
        self.canvas = Canvas(self.figure)
        self.theplot = self.figure.add_subplot(111)        

        self.theplot.set_title(title)
        self.theplot.set_xlabel(xlabel)
        self.theplot.set_ylabel(ylabel)

    def plotDataPoints(self, x, y):
        self.theplot.plot(x,y)
        self.draw()            
##################################################


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(649, 501)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 30, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        
        self.matplotlibwidget = MatplotlibWidget(Form)
        self.matplotlibwidget.setGeometry(QtCore.QRect(130, 80, 400, 300))
        self.matplotlibwidget.setObjectName(_fromUtf8("matplotlibwidget"))
        self.matplotlibwidget.plotDataPoints(x,y) 
        
        self.dial = QtGui.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(30, 90, 50, 64))
        self.dial.setObjectName(_fromUtf8("dial"))
        
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_2.setNum)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.matplotlibwidget.update)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Function: Sin(w.t)", None))
        self.label_2.setText(_translate("Form", "TextLabel", None))

from matplotlibwidget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

