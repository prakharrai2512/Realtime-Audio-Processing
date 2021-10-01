from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
import pyaudio
import matplotlib.pyplot as plt
import numpy as np
import sys
from Qtpy.uijsr import *
from Audio_Exec import device_list as dlist

aud_list = dlist.retlist()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec()