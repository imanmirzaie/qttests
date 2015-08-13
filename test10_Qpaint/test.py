# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Thu Sep 11 00:48:16 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(608, 673)
        self.dial = QtGui.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(110, 490, 111, 141))
        self.dial.setObjectName(_fromUtf8("dial"))
        self.dial_2 = QtGui.QDial(Form)
        self.dial_2.setGeometry(QtCore.QRect(370, 490, 111, 131))
        self.dial_2.setObjectName(_fromUtf8("dial_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 470, 46, 16))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(390, 470, 46, 16))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.imagewidget = ImageWidget(Form)
        self.imagewidget.setGeometry(QtCore.QRect(90, 60, 400, 300))
        self.imagewidget.setOrientation(QtCore.Qt.Vertical)
        self.imagewidget.setObjectName(_fromUtf8("imagewidget"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "X", None))
        self.label_2.setText(_translate("Form", "Y", None))

from guiqwt.plot import ImageWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

