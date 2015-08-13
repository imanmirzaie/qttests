from PyQt4 import QtCore, QtGui
from matplotlibwidget import MatplotlibWidget
import numpy as np

global y
global x
x=[1,2,3]
y=[1, 2, 1]

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.mplwidget = MatplotlibWidget(self.centralwidget)
        self.mplwidget.setGeometry(QtCore.QRect(170, 150, 400, 300))
        self.mplwidget.setObjectName("mplwidget")
        self.mplwidget.setFocus()
        self.mplwidget.axes.plot(x,y)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtGui.QStatusBar(MainWindow) 
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")        

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.plot)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def plot(self):   
        global y
        global x
        x = [2,3,4]
        y = [2,2,1]
        self.replot()

    def replot(self):
        Ui_MainWindow()
        ui.setupUi(MainWindow)        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())