# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner.ui'
#
# Created: Tue Aug  5 16:20:08 2014
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

class Ui_MplMainWindow(object):
    def setupUi(self, MplMainWindow):
        MplMainWindow.setObjectName(_fromUtf8("MplMainWindow"))
        MplMainWindow.resize(800, 600)
        self.mplcentralwidget = QtGui.QWidget(MplMainWindow)
        self.mplcentralwidget.setObjectName(_fromUtf8("mplcentralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.mplcentralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mplhorizontalLayout = QtGui.QHBoxLayout()
        self.mplhorizontalLayout.setObjectName(_fromUtf8("mplhorizontalLayout"))
        self.mpllineEdit = QtGui.QLineEdit(self.mplcentralwidget)
        self.mpllineEdit.setObjectName(_fromUtf8("mpllineEdit"))
        self.mplhorizontalLayout.addWidget(self.mpllineEdit)
        self.mplpushButton = QtGui.QPushButton(self.mplcentralwidget)
        self.mplpushButton.setObjectName(_fromUtf8("mplpushButton"))
        self.mplhorizontalLayout.addWidget(self.mplpushButton)
        self.verticalLayout.addLayout(self.mplhorizontalLayout)
        self.mpl = MplWidget(self.mplcentralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setObjectName(_fromUtf8("mpl"))
        self.verticalLayout.addWidget(self.mpl)
        MplMainWindow.setCentralWidget(self.mplcentralwidget)
        self.mplmenubar = QtGui.QMenuBar(MplMainWindow)
        self.mplmenubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.mplmenubar.setObjectName(_fromUtf8("mplmenubar"))
        self.mplmenuFile = QtGui.QMenu(self.mplmenubar)
        self.mplmenuFile.setObjectName(_fromUtf8("mplmenuFile"))
        MplMainWindow.setMenuBar(self.mplmenubar)
        self.mplactionOpen = QtGui.QAction(MplMainWindow)
        self.mplactionOpen.setObjectName(_fromUtf8("mplactionOpen"))
        self.mplactionQuit = QtGui.QAction(MplMainWindow)
        self.mplactionQuit.setObjectName(_fromUtf8("mplactionQuit"))
        self.mplmenuFile.addAction(self.mplactionOpen)
        self.mplmenuFile.addSeparator()
        self.mplmenuFile.addAction(self.mplactionQuit)
        self.mplmenubar.addAction(self.mplmenuFile.menuAction())

        self.retranslateUi(MplMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MplMainWindow)

    def retranslateUi(self, MplMainWindow):
        MplMainWindow.setWindowTitle(_translate("MplMainWindow", "MainWindow", None))
        self.mplpushButton.setText(_translate("MplMainWindow", "PushButton", None))
        self.mplmenuFile.setTitle(_translate("MplMainWindow", "File", None))
        self.mplactionOpen.setText(_translate("MplMainWindow", "Open", None))
        self.mplactionQuit.setText(_translate("MplMainWindow", "Quit", None))

from mplwidget import MplWidget
