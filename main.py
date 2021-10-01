from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
import pyaudio
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np
import sys
from Qtpy.uijsr import *
from Qtpy.mplCanv import *
import Audio_Exec.aud_stream as adbf
from Audio_Exec import device_list as dlist
import time
from Audio_Exec.aud_stream import audBuffer,rate,bufL
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


def jsr():
    print("JSR")

""" def plotty():
    t1 = time.time()
    saveAs=r"03.png"
    while True:
        if (time.time()-t1)>0.25:
            t1=time.time()
            pylab.plot(np.arange(len(audBuffer))/rate,audBuffer)
            pylab.axis([0,bufL,-2**16/2,2**16/2])
            pylab.show()
            if saveAs:
                pylab.savefig(saveAs,dpi=50)
            else:
                pylab.show()
            pylab.close('all') 
 """
def jsrplot():
    ui.canvas = MplCanvas(width=8, height=6, dpi=100)
    MainWindow.setCentralWidget(ui.canvas)
    #ui.canvas.plot_refs = None
    update_plot()

    ui.timer = QtCore.QTimer()
    ui.timer.setInterval(100)
    ui.timer.timeout.connect(update_plot)
    ui.timer.start()


def update_plot():
    print("Hewwwo")
    ui.canvas.axes.cla() 
    ui.canvas.axes.autoscale(True)
    ui.canvas.axes.plot(np.arange(len(audBuffer))/rate,audBuffer)
    ui.canvas.draw()
    """ if ui.canvas.plot_refs is None:
        plot_refs = ui.canvas.axes.plot(np.arange(len(audBuffer))/rate,audBuffer,'b')
        ui.canvas.plot_ref = plot_refs[0]
    else:
        ui.canvas.plot_refs.set_ydata(audBuffer)

        # Trigger the canvas to update and redraw.
    ui.canvas.draw() """

def jsrspec():
    ui.canvas = MplCanvas(width=8, height=6, dpi=100)
    MainWindow.setCentralWidget(ui.canvas)
    ui.canvas._plot_ref = None
    update_plot1()
    ui.timer = QtCore.QTimer()
    ui.timer.setInterval(100)
    ui.timer.timeout.connect(update_plot1)
    ui.timer.start()


def update_plot1():
    print("Hewwwo")
    ui.canvas.axes.cla() 
    ui.canvas.axes.autoscale(True)
    ui.canvas.axes.specgram(audBuffer,Fs=rate)
    ui.canvas.draw()


def add_dev():
    for i in aud_list.keys():
        ui.devcombo.addItem(i)
    ui.devcombo.setCurrentIndex(0)

def audstream():
    bigT = ui.devcombo.currentText()
    adbf.audthread(aud_list[bigT])


aud_list = dlist.retlist()
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)


add_dev()
MainWindow.show()
ui.ampwave.clicked.connect(jsrplot)
ui.conDev.clicked.connect(audstream)
ui.spect.clicked.connect(jsrspec)
app.exec()

adbf.kilBoi()


