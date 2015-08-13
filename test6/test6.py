# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test6.ui'
#
# Created: Wed Aug  6 14:25:19 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(896, 672)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.Widget1 = QtGui.QWidget(self.centralwidget)
        self.Widget1.setGeometry(QtCore.QRect(500, 30, 331, 291))
        self.Widget1.setObjectName(_fromUtf8("Widget1"))
        
        self.dial1 = QtGui.QDial(self.Widget1)
        self.dial1.setGeometry(QtCore.QRect(80, 120, 180, 190))
        self.dial1.setObjectName(_fromUtf8("dial1"))
        
        self.lcdNumber1 = QtGui.QLCDNumber(self.Widget1)
        self.lcdNumber1.setGeometry(QtCore.QRect(80, 30, 181, 101))
        self.lcdNumber1.setObjectName(_fromUtf8("lcdNumber1"))
        
        self.Widget0 = QtGui.QWidget(self.centralwidget)
        self.Widget0.setGeometry(QtCore.QRect(100, 30, 341, 291))
        self.Widget0.setObjectName(_fromUtf8("Widget0"))
        
        self.dial0 = QtGui.QDial(self.Widget0)
        self.dial0.setGeometry(QtCore.QRect(80, 120, 180, 190))
        self.dial0.setObjectName(_fromUtf8("dial0"))
        
        self.lcdNumber0 = QtGui.QLCDNumber(self.Widget0)
        self.lcdNumber0.setGeometry(QtCore.QRect(70, 30, 191, 101))
        self.lcdNumber0.setObjectName(_fromUtf8("lcdNumber0"))
        
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(330, 380, 281, 141))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 896, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.dial0, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber0.display)
        QtCore.QObject.connect(self.dial1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber1.display)
        QtCore.QObject.connect(self.dial0, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.adder)
        QtCore.QObject.connect(self.dial1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.adder)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def adder(self,MainWindow):
        self.lcdNumber.display(self.dial0.value()+self.dial1.value())
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

