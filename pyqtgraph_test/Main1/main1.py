# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:56:05 2015

@author: iman
"""
from PySide import QtCore, QtGui, QtUiTools
import test1
import numpy as np
import pyaudio
#import wave



form = test1.Ui_Form()



def setup_main(parent):
    form.setupUi(parent)
    QtCore.QObject.connect(form.pushButton_plot, QtCore.SIGNAL("clicked()"), plot)
    QtCore.QObject.connect(form.pushButton_measure,QtCore.SIGNAL('clicked()'),measure)


def plot():
    global frames
    pw = form.graphicsView
    pw.clear()
    p1 = pw.plot()
    dat_plot =  np.fromstring(np.array(frames),dtype='int16')
    p1.setData(y=dat_plot)



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


