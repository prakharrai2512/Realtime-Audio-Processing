from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
import pyaudio
import matplotlib.pyplot as plt
import numpy as np
import sys
from Qtpy.uijsr import *
import Audio_Exec.aud_stream as adbf
from Audio_Exec import device_list as dlist
import time

killAudthread = False


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


ui.conDev.clicked.connect(audstream)
add_dev()
MainWindow.show()
app.exec()
adbf.kilBoi()
