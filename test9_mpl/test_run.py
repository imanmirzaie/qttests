# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Sun Aug 10 20:12:10 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!


###########################################################################
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PyQt4'

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np
###########################################################################


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
    
    x = np.linspace(0,10,100)
    y = np.sin(x)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.mplWidget = QtGui.QWidget(self.centralwidget)
        self.mplWidget.setGeometry(QtCore.QRect(350, 0, 450, 341))
        self.mplWidget.setObjectName(_fromUtf8("mplWidget"))
        
###########################################################################
        self.fig = Figure(figsize=(5,4))
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(self.x,self.y)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.mplWidget)
        #self.canvas.adjustSize(self.mplWidget.size())
###########################################################################
        
        self.plotButton = QtGui.QPushButton(self.centralwidget)
        self.plotButton.setGeometry(QtCore.QRect(130, 80, 75, 23))
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        
        self.freqBox = QtGui.QSpinBox(self.centralwidget)
        self.freqBox.setGeometry(QtCore.QRect(140, 170, 42, 22))
        self.freqBox.setObjectName(_fromUtf8("freqBox"))
        self.freqBox.setProperty("value", 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.plotButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.replot)
        QtCore.QObject.connect(self.freqBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.freqUpdate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def replot(self):
        self.ax.clear()
        self.ax.plot(self.x,self.y)
        self.canvas.draw()
    
    def freqUpdate(self):
        w = self.freqBox.value()
        self.y = np.sin(w*self.x)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.plotButton.setText(_translate("MainWindow", "Plot!", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

