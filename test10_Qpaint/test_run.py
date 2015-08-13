# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Thu Sep 11 00:01:40 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

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

    # Frame dimensions 
    x0_f = 300; y0_f = 300; w0_f = 500; h0_f = 350;   
    
    # Absolute dimensions
    x0 = 0
    y0 = h0_f
    
    # Substrate dimensions 
    sub_h = -50
    sub_w = w0_f
    
    # Under layer dimensions
    ul_w = 50
    ul_h = -100
    
    # Undercut depth
    uc_d = 80    
    
    # Over layer dimensions
    ol_w = ul_w + uc_d
    ol_h = -20
    

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(608, 673)
        
        self.imagewidget = QtGui.QImage(QtCore.QSize(100,100),QtGui.QImage.Format(4))
        self.imagewidget.fill(1)
        #self.imagewidget.setGeometry(QtCore.QRect(90, 60, 400, 300))
        #self.imagewidget.setOrientation(QtCore.Qt.Vertical)
        #self.imagewidget.setObjectName(_fromUtf8("imagewidget"))
        
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

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.drawShape)
        QtCore.QObject.connect(self.dial_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.drawShape)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def drawShape(self,Form):
        p = QtGui.QPainter()
        p.begin(self.imagewidget)
        
        # optional
        p.setRenderHint(QtGui.QPainter.Antialiasing)
        
        # make a white drawing background
        #p.setBrush(QtCore.Qt.white)
        #p.drawRect(event.rect())
        
        
        # Construct substrate
        subst = QtCore.QRectF(self.x0, self.y0, self.sub_w, self.sub_h )
        
        # Construct underlayer
        ul = QtCore.QRectF(self.x0, self.y0 + self.sub_h, self.ul_w, self.ul_h)
        
        # Constructing over layer
        ol = QtCore.QRectF(self.x0, self.y0 + self.sub_h + self.ul_h, self.ol_w, self.ol_h)
        
        
        rects = [subst, ul, ol]
        colors = [QtGui.QColor('black'),QtGui.QColor('red'),QtGui.QColor('green')]
        
        for i in range(len(rects)):
            p.drawRect(rects[i])
            p.fillRect(rects[i],colors[i])
        
        
        
        p.end()


        
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "X", None))
        self.label_2.setText(_translate("Form", "Y", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

