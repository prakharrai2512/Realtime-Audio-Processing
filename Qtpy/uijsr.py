# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Qtui\Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 656)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:#1d1d1d;\n"
"\n"
"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.devcombo = QtWidgets.QComboBox(self.centralwidget)
        self.devcombo.setGeometry(QtCore.QRect(340, 220, 511, 51))
        self.devcombo.setStyleSheet("background-color:rgb(254, 254, 254);\n"
"color:black;\n"
"border-radius:5px;\n"
"border-style:bold;\n"
"font-size:20px;\n"
"padding-left:10%;")
        self.devcombo.setIconSize(QtCore.QSize(20, 20))
        self.devcombo.setObjectName("devcombo")
        self.conDev = QtWidgets.QPushButton(self.centralwidget)
        self.conDev.setGeometry(QtCore.QRect(470, 380, 251, 61))
        self.conDev.setStyleSheet("background-color:white;\n"
"border-style:dashed;\n"
"border-radius:10px;\n"
"font-size:24px;\n"
"font-family: \"MS UI Gothic\";\n"
"\n"
"/*background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #22c1c3, stop:1 #fdbb2d);*/\n"
"\n"
"")
        self.conDev.setObjectName("conDev")
        self.ampwave = QtWidgets.QPushButton(self.centralwidget)
        self.ampwave.setGeometry(QtCore.QRect(790, 380, 261, 61))
        self.ampwave.setStyleSheet("background-color:white;\n"
"border-style:dashed;\n"
"border-radius:10px;\n"
"font-size:24px;\n"
"font-family: \"MS UI Gothic\";\n"
"")
        self.ampwave.setObjectName("ampwave")
        self.spect = QtWidgets.QPushButton(self.centralwidget)
        self.spect.setGeometry(QtCore.QRect(140, 380, 251, 61))
        self.spect.setStyleSheet("background-color:white;\n"
"border-style:dashed;\n"
"border-radius:10px;\n"
"font-size:24px;\n"
"font-family: \"MS UI Gothic\";\n"
"")
        self.spect.setObjectName("spect")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 50, 861, 61))
        self.label.setStyleSheet("color:white;\n"
"font-size:30px;\n"
"text-align: center;\n"
"font-family: \"MS UI Gothic\";\n"
"position:absolute;\n"
"padding-left:100%;\n"
"padding-right:100%;")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Realtime Audio Analysis"))
        self.conDev.setText(_translate("MainWindow", "Connect to Device"))
        self.ampwave.setText(_translate("MainWindow", "Amplitude Wave"))
        self.spect.setText(_translate("MainWindow", "Spectogram"))
        self.label.setText(_translate("MainWindow", "Choose the input device that you want to analyze"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
