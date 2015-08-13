# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgTest.ui'
#
# Created: Sun Jul 19 10:02:53 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgMPLTest(object):
    def setupUi(self, dlgMPLTest):
        dlgMPLTest.setObjectName("dlgMPLTest")
        dlgMPLTest.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(dlgMPLTest)
        self.gridLayout.setObjectName("gridLayout")
        self.widgetPlot = QtGui.QWidget(dlgMPLTest)
        self.widgetPlot.setObjectName("widgetPlot")
        self.gridLayout.addWidget(self.widgetPlot, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(dlgMPLTest)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(dlgMPLTest)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dlgMPLTest.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dlgMPLTest.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgMPLTest)

    def retranslateUi(self, dlgMPLTest):
        dlgMPLTest.setWindowTitle(QtGui.QApplication.translate("dlgMPLTest", "MPL Test", None, QtGui.QApplication.UnicodeUTF8))

