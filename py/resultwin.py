# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ocsen\PycharmProjects\Szakdoga\pyqt lapok\resultwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *
import sys
import json

from ques11 import *
class Ui_resultwin(QtWidgets.QWidget):
    def __init__(self, name, count, total):
        super().__init__()
        self.name = name
        self.count = count
        self.total = total
        self.S1 = str(self.count // 60)
        self.S2 = str(self.count % 60)
        self.S3 = self.S1 + ":" + self.S2

    def setupUi(self, resultwin):
        resultwin.setObjectName("resultwin")
        resultwin.resize(1024, 720)
        self.centralwidget = QtWidgets.QWidget(resultwin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1024, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            "képek/fuvespuszta.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(350, 270, 301, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                      "    background: rgb(0, 170, 255);\n"
                                      "    border: 2px solid rgb(0, 117, 176);\n"
                                      "    border-radius: 10px;\n"
                                      "}")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                      "    background: rgb(0, 170, 255);\n"
                                      "    border: 2px solid rgb(0, 117, 176);\n"
                                      "    border-radius: 10px;\n"
                                      "}")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
                              "    background: rgb(0, 170, 255);\n"
                              "    border: 2px solid rgb(0, 117, 176);\n"
                              "    border-radius: 10px;\n"
                              "}")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 200, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(350, 460, 301, 51))
        self.B1.setStyleSheet("QPushButton{\n"
                              "    background: rgb(0, 170, 255);\n"
                              "    border: 2px solid rgb(0, 117, 176);\n"
                              "    border-radius: 10px;\n"
                              "}")
        self.B1.setObjectName("B1")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(450, 380, 91, 51))
        self.button.setObjectName("button")
        self.button.setStyleSheet("QPushButton{\n"
                              "    background: rgb(0, 170, 255);\n"
                              "    border: 2px solid rgb(0, 117, 176);\n"
                              "    border-radius: 10px;\n"
                              "}")
        self.mentesgomb = QtWidgets.QPushButton(self.centralwidget)
        self.mentesgomb.setGeometry(QtCore.QRect(370, 530, 261, 41))
        self.mentesgomb.setStyleSheet("QPushButton{\n"
                              "background: rgb(0, 170, 255);\n"
                              "border: 2px solid rgb(0, 117, 176);\n"
                              "border-radius: 5px;\n"
                              "}")
        self.mentesgomb.setObjectName("mentesgomb")
        resultwin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(resultwin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        resultwin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(resultwin)
        self.statusbar.setObjectName("statusbar")
        resultwin.setStatusBar(self.statusbar)

        self.retranslateUi(resultwin)
        QtCore.QMetaObject.connectSlotsByName(resultwin)

        self.button.clicked.connect(self.show_popup)

    def retranslateUi(self, resultwin):
        _translate = QtCore.QCoreApplication.translate
        resultwin.setWindowTitle(_translate("resultwin", "Játékos matematikai gyakorlóprogram"))
        self.label_2.setText(_translate("resultwin", "Becenév: "))
        self.label_3.setText(_translate("resultwin", "Hátralévő idő:"))
        self.label_4.setText(_translate("resultwin", "Szerzett pontszám:"))
        self.label_5.setText(_translate("resultwin", "Füves Puszta | Eredmény"))
        self.B1.setText(_translate("resultwin", "Tovább"))
        self.button.setText(_translate("resultwin", "?"))
        self.mentesgomb.setText(_translate("resultwin", "Mentés"))
        self.lineEdit.setText(str(self.name))
        self.lineEdit_2.setText(str(self.S3))
        self.lineEdit_3.setText(str(self.total))
        self.B1.clicked.connect(self.opques)
        self.B1.clicked.connect(resultwin.hide)
        self.mentesgomb.clicked.connect(self.json)

    def readjson(self):
        file_path = "mentesek.json"

        try:
            with open(file_path, mode="r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except Exception as e:
            return []

    def find_in_list(self, lst):
        return [x for x in lst if x["becenev"] == self.name]


    def json(self):
        data = {
            "becenev": self.name,
            "elert pontszam": self.total,
            "teljesitett palya": "fuvespuszta"
        }

        lst = self.readjson()

        players = self.find_in_list(lst)
        if len(players) > 0:
            players[0]["elert pontszam"] = self.total
            players[0]["teljesitett palya"] = "fuvespuszta"
        else:
            lst.append(data)

        file_path = "mentesek.json"

        try:
            with open(file_path, mode="w", encoding='utf-8') as json_file:
                json.dump(lst, json_file, indent=4)
            QMessageBox.information(self, "Sikeres mentés!",
                                    "Sikeresen elmentetted az előrehaladásod! "
                                    "A főmenüben a mentések betöltése nevezetű gombnál "
                                    "egyből ide tudsz ugrani és innen folytatni.")
        except Exception as e:
            QMessageBox.critical(self, "Hiba!", f"Hiba történt "
                                                f"a mentés folyamán: {str(e)}")

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Füves puszta teljesítve!")
        msg.setText(
            "Gratulálok az első szint teljesítéséhez!")
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()

    def opques(self):
        self.queswin = QtWidgets.QMainWindow()
        self.ui = Ui_ques11(self.name, self.total)
        self.ui.setupUi(self.queswin)
        self.queswin.show()
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    resultwin = QtWidgets.QMainWindow()
    ui = Ui_resultwin("b", 23, 25)
    ui.setupUi(resultwin)
    resultwin.show()
    sys.exit(app.exec_())