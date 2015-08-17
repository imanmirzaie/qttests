# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:56:05 2015

@author: iman
"""
from PySide import QtCore, QtGui, QtUiTools
import test1
import numpy as np
import pyaudio
import time
#import wave


form = test1.Ui_Form()


def setup_main(parent):
    form.setupUi(parent)
    QtCore.QObject.connect(form.pushButton_plot, QtCore.SIGNAL("clicked()"), plot)
    QtCore.QObject.connect(form.pushButton_measure,QtCore.SIGNAL('clicked()'),measure)
    QtCore.QObject.connect(form.pushButton_liveStart,QtCore.SIGNAL('clicked()'),live_start)


def live_start():
    while 1:
        measure()
        time.sleep(3)
        plot()
        time.sleep(1)

def plot():
    global frames

    yr =  np.fromstring(np.array(frames),dtype='int16')
    xr = np.arange(len(yr))

    pw = form.graphicsView_time
    pw.clear()
    pw.setXRange(xr[0],xr[-1])
    pw.setYRange(yr.min(),yr.max())

    p1 = pw.plot()
    p1.setData(y=yr,x=xr)


def measure():
    global frames
    # save audio data into an object
    aud_chunk = 1024
    aud_format = pyaudio.paInt16
    aud_channels = 2
    aud_rate = 44100
    aud_rec_seconds = 2

    p = pyaudio.PyAudio()

    stream = p.open(format=aud_format,
                    channels=aud_channels,
                    rate=aud_rate,
                    input=True,
                    frames_per_buffer=aud_chunk)

    print("* recording")

    frames = []

    for i in range(0, int(aud_rate / aud_chunk * aud_rec_seconds)):
        data = stream.read(aud_chunk)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()






if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    setup_main(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


