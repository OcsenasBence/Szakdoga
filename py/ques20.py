# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ocsen\Desktop\szakdoga pyqt lapok\pálya20.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from resultwin2 import *



class Ui_ques20(QtWidgets.QWidget):
    def __init__(self, name, count, total):
        super().__init__()
        self.name = name
        self.count = count
        self.total = total

    def setupUi(self, ques20):
        ques20.setObjectName("ques20")
        ques20.resize(1024, 720)
        ques20.setMinimumSize(QtCore.QSize(1024, 720))
        ques20.setMaximumSize(QtCore.QSize(1024, 720))
        self.centralwidget = QtWidgets.QWidget(ques20)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1024, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("képek/esoerdo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 70, 261, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
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
                              "    background: rgb(45, 208, 0);\n"
                              "    border: 2px solid rgb(31, 141, 0);\n"
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
                              "    background: rgb(45, 208, 0);\n"
                              "    border: 2px solid rgb(31, 141, 0);\n"
                              "    border-radius: 10px;\n"
                              "}")
        self.horizontalLayout.addWidget(self.T2)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(300, 390, 411, 251))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
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
        self.B1 = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.B1.setFont(font)
        self.B1.setObjectName("B1")
        self.B1.setStyleSheet("QPushButton{\n"
                              "    background: rgb(45, 208, 0);\n"
                              "    border: 2px solid rgb(31, 141, 0);\n"
                              "    border-radius: 10px;\n"
                              "}")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.B1)
        self.R4 = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R4.setFont(font)
        self.R4.setObjectName("R4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.R4)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 280, 150, 71))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        ques20.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ques20)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        ques20.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ques20)
        self.statusbar.setObjectName("statusbar")
        ques20.setStatusBar(self.statusbar)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ShowTime)
        self.timer.start(1000)
        self.retranslateUi(ques20)
        QtCore.QMetaObject.connectSlotsByName(ques20)

    def retranslateUi(self, ques20):
        _translate = QtCore.QCoreApplication.translate
        ques20.setWindowTitle(_translate("ques20", "Játékos matematikai gyakorlóprogram"))
        self.label_4.setText(_translate("ques20", "Esőerdő | Tizedik feladat"))
        self.label_2.setText(_translate("ques20", "Becenév:"))
        self.label_3.setText(_translate("ques20", "Hátralévő idő:"))
        self.label_5.setText(_translate("ques20", "10. feladat: Végezd el az alábbi műveletet!"))
        self.R1.setText(_translate("ques20", "12,6"))
        self.R2.setText(_translate("ques20", "12,7"))
        self.R3.setText(_translate("ques20", "12,8"))
        self.B1.setText(_translate("ques20", "Következő"))
        self.R4.setText(_translate("ques20", "12,9"))
        self.label_6.setText(_translate("ques20",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">38,7 : 3 =</span></p></body></html>"))
        self.B1.clicked.connect(self.opques)
        self.B1.clicked.connect(ques20.close)

    def ShowTime(self):
        if self.count > 0:
            self.count = self.count - 1
        S1 = str(self.count // 60)
        S2 = str(self.count % 60)
        S3 = S1 + ":" + S2
        self.T1.setText(str(self.name))
        self.T2.setText(S3)
        self.T1.setEnabled(False)
        self.T2.setEnabled(False)

    def opques(self):
        if self.R1.isChecked() == True:
            self.total = self.total - 1
        if self.R2.isChecked() == True:
            self.total = self.total - 1
        if self.R3.isChecked() == True:
            self.total = self.total - 1
        if self.R4.isChecked() == True:
            self.total = self.total + 3
        self.queswin = QtWidgets.QMainWindow()
        self.ui = Ui_resultwin2(self.name, self.count, self.total)
        self.ui.setupUi(self.queswin)
        self.queswin.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ques20 = QtWidgets.QMainWindow()
    ui = Ui_ques20()
    ui.setupUi(ques20)
    ques20.show()
    sys.exit(app.exec_())
