# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ocsen\Desktop\szakdoga pyqt lapok\pálya6.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from ques7 import *

class Ui_ques6(QtWidgets.QWidget):
    def __init__(self, name, count, total):
        super().__init__()
        self.name = name
        self.count = count
        self.total = total
    def setupUi(self, ques6):
        ques6.setObjectName("ques6")
        ques6.resize(1024, 720)
        ques6.setMinimumSize(QtCore.QSize(1024, 720))
        ques6.setMaximumSize(QtCore.QSize(1024, 720))
        self.centralwidget = QtWidgets.QWidget(ques6)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1024, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("képek/fuvespuszta.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 60, 311, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 140, 591, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.T1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T1.sizePolicy().hasHeightForWidth())
        self.T1.setSizePolicy(sizePolicy)
        self.T1.setObjectName("T1")
        self.T1.setStyleSheet("QLineEdit{\n"
                              "    background: rgb(0, 170, 255);\n"
                              "    border: 2px solid rgb(0, 117, 176);\n"
                              "    border-radius: 10px;\n"
                              "}")
        self.horizontalLayout.addWidget(self.T1)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.T2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T2.sizePolicy().hasHeightForWidth())
        self.T2.setSizePolicy(sizePolicy)
        self.T2.setObjectName("T2")
        self.T2.setStyleSheet("QLineEdit{\n"
                              "    background: rgb(0, 170, 255);\n"
                              "    border: 2px solid rgb(0, 117, 176);\n"
                              "    border-radius: 10px;\n"
                              "}")
        self.horizontalLayout.addWidget(self.T2)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(300, 390, 411, 251))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.R1 = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R1.setFont(font)
        self.R1.setObjectName("R1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.R1)
        self.R2 = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R2.setFont(font)
        self.R2.setObjectName("R2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.R2)
        self.R3 = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R3.setFont(font)
        self.R3.setObjectName("R3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.R3)
        self.R4 = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R4.setFont(font)
        self.R4.setObjectName("R4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.R4)
        self.B1 = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.B1.setFont(font)
        self.B1.setObjectName("B1")
        self.B1.setStyleSheet("QPushButton{\n"
                              "    background: rgb(0, 170, 255);\n"
                              "    border: 2px solid rgb(0, 117, 176);\n"
                              "    border-radius: 10px;\n"
                              "}")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.B1)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 260, 131, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("képek/6. feladat képe.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        ques6.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ques6)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        ques6.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ques6)
        self.statusbar.setObjectName("statusbar")
        ques6.setStatusBar(self.statusbar)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ShowTime)
        self.timer.start(1000)
        self.retranslateUi(ques6)
        QtCore.QMetaObject.connectSlotsByName(ques6)

    def retranslateUi(self, ques6):
        _translate = QtCore.QCoreApplication.translate
        ques6.setWindowTitle(_translate("ques6", "Játékos matematikai gyakorlóprogram"))
        self.label_4.setText(_translate("ques6", "Füves puszta | Hatodik feladat"))
        self.label_2.setText(_translate("ques6", "Becenév:"))
        self.label_3.setText(_translate("ques6", "Hátralévő idő:"))
        self.R1.setText(_translate("ques6", "7"))
        self.R2.setText(_translate("ques6", "6"))
        self.R3.setText(_translate("ques6", "5"))
        self.R4.setText(_translate("ques6", "4"))
        self.B1.setText(_translate("ques6", "Következő"))
        self.label_5.setText(_translate("ques6", "6. feladat: Melyik szám van a négyzet alatt?"))
        self.B1.clicked.connect(self.opques)
        self.B1.clicked.connect(ques6.hide)

    def ShowTime(self):
        if self.count > 0:
            self.count = self.count - 1
        S1 = str(self.count//60)
        S2 = str(self.count%60)
        S3 = S1 + ":" + S2
        self.T1.setText(str(self.name))
        self.T2.setText(S3)
        self.T1.setEnabled(False)
        self.T2.setEnabled(False)

    def opques(self):
        if self.R1.isChecked() == True:
            self.total = self.total - 1
        if self.R2.isChecked() == True:
            self.total = self.total + 3
        if self.R3.isChecked() == True:
            self.total = self.total - 1
        if self.R4.isChecked() == True:
            self.total = self.total - 1
        self.queswin = QtWidgets.QMainWindow()
        self.ui = Ui_ques7(self.name,self.count,self.total)
        self.ui.setupUi(self.queswin)
        self.queswin.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ques6 = QtWidgets.QMainWindow()
    ui = Ui_ques6()
    ui.setupUi(ques6)
    ques6.show()
    sys.exit(app.exec_())
