# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created: Fri Aug 14 20:58:49 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(911, 696)
        self.graphicsView = PlotWidget(Form)
        self.graphicsView.setGeometry(QtCore.QRect(450, 10, 451, 301))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_plot = QtGui.QPushButton(Form)
        self.pushButton_plot.setGeometry(QtCore.QRect(130, 460, 83, 24))
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.pushButton_measure = QtGui.QPushButton(Form)
        self.pushButton_measure.setGeometry(QtCore.QRect(130, 500, 83, 24))
        self.pushButton_measure.setObjectName("pushButton_measure")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_plot.setText(QtGui.QApplication.translate("Form", "Plot!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_measure.setText(QtGui.QApplication.translate("Form", "Measure", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
