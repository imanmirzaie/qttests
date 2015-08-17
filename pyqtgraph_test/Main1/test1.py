# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created: Sat Aug 15 21:57:48 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(911, 696)
        self.graphicsView_time = PlotWidget(Form)
        self.graphicsView_time.setGeometry(QtCore.QRect(450, 10, 451, 301))
        self.graphicsView_time.setObjectName("graphicsView_time")
        self.pushButton_plot = QtGui.QPushButton(Form)
        self.pushButton_plot.setGeometry(QtCore.QRect(130, 400, 83, 24))
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.pushButton_measure = QtGui.QPushButton(Form)
        self.pushButton_measure.setGeometry(QtCore.QRect(130, 440, 83, 24))
        self.pushButton_measure.setObjectName("pushButton_measure")
        self.graphicsView_freq = PlotWidget(Form)
        self.graphicsView_freq.setGeometry(QtCore.QRect(450, 320, 451, 301))
        self.graphicsView_freq.setObjectName("graphicsView_freq")
        self.pushButton_liveStart = QtGui.QPushButton(Form)
        self.pushButton_liveStart.setGeometry(QtCore.QRect(130, 540, 83, 24))
        self.pushButton_liveStart.setObjectName("pushButton_liveStart")
        self.pushButton_liveStop = QtGui.QPushButton(Form)
        self.pushButton_liveStop.setGeometry(QtCore.QRect(130, 580, 83, 24))
        self.pushButton_liveStop.setObjectName("pushButton_liveStop")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_plot.setText(QtGui.QApplication.translate("Form", "Plot!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_measure.setText(QtGui.QApplication.translate("Form", "Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_liveStart.setText(QtGui.QApplication.translate("Form", "Live start", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_liveStop.setText(QtGui.QApplication.translate("Form", "Live stop", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
