# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:56:05 2015

@author: iman
"""
from PySide import QtCore, QtGui, QtUiTools
import test1
import numpy as np

form = test1.Ui_Form()


def setup_main(parent):
    form.setupUi(parent)
    QtCore.QObject.connect(form.pushButton, QtCore.SIGNAL("clicked()"), plot)


def plot():
    print('test')
    pw = form.graphicsView
    pw.clear()
    p1 = pw.plot()
    rect = QtGui.QGraphicsRectItem(QtCore.QRectF(0, 0, 1, 5e-11))
    rect.setPen(QtGui.QPen(QtGui.QColor(100, 200, 100)))
    pw.addItem(rect)

    yd, xd = rand(10000)
    p1.setData(y=yd, x=xd)


def rand(n):
    data = np.random.random(n)
    data[int(n*0.1):int(n*0.13)] += .5
    data[int(n*0.18)] += 2
    data[int(n*0.1):int(n*0.13)] *= 5
    data[int(n*0.18)] *= 20
    data *= 1e-12
    return data, np.arange(n, n+len(data)) / float(n)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    setup_main(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


