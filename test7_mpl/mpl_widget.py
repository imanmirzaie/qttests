# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mpl_widget.ui'
#
# Created: Sun Aug 10 14:27:50 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import numpy as np

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

    x = np.linspace(-10,10,500)
    y = np.sin(x)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.mplw = MatplotlibWidget(self.centralwidget)
        self.mplw.setGeometry(QtCore.QRect(189, 40, 511, 421))
        self.mplw.setObjectName(_fromUtf8("mplw"))
        self.mplw.setFocus()
        #self.mplw.axes.plot(self.x,self.y)
        
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 50, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 110, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.msgTest)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.draw)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Sin(x)", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cos(x)", None))
        self.pushButton.setText(_translate("MainWindow", "Draw!", None))
    
    def msgTest(self):
        print('Current index:',self.comboBox.currentIndex())
    
    def draw(self):
        self.mplw.setFocus()
        self.mplw.axes.plot(self.x,self.y)
    
    def selectGraph(self):
        if (self.comboBox.currentIndex() == 0):
            self.y = np.sin(self.x)
        if (self.comboBox.currentIndex() == 1):
            self.y = np.cos(self.x)
            
from matplotlibwidget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

