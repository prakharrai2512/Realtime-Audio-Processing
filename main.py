from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
import pyaudio
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np
import sys
from Qtpy.uijsr import *
import Audio_Exec.aud_stream as adbf
from Audio_Exec import device_list as dlist
import time
from Audio_Exec.aud_stream import audBuffer,rate,bufL

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
ui.ampwave.clicked.connect(jsr)
ui.conDev.clicked.connect(audstream)
app.exec()

adbf.kilBoi()


