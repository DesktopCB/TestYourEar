# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chose_guitar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Guitar(object):
    def chose(self, chose_guitar):
        chose_guitar.setObjectName("chose_guitar")
        chose_guitar.resize(1280, 720)
        chose_guitar.setMinimumSize(QtCore.QSize(1280, 720))
        chose_guitar.setMaximumSize(QtCore.QSize(1280, 720))
        chose_guitar.setStyleSheet("background-color: rgb(255, 255, 102);")
        self.centralwidget = QtWidgets.QWidget(chose_guitar)
        self.centralwidget.setObjectName("centralwidget")
        self.medium = QtWidgets.QPushButton(self.centralwidget)
        self.medium.setGeometry(QtCore.QRect(540, 340, 200, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(25)
        self.medium.setFont(font)
        self.medium.setObjectName("medium")
        self.hard = QtWidgets.QPushButton(self.centralwidget)
        self.hard.setGeometry(QtCore.QRect(540, 430, 200, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(25)
        self.hard.setFont(font)
        self.hard.setObjectName("hard")
        self.chose_text = QtWidgets.QLabel(self.centralwidget)
        self.chose_text.setGeometry(QtCore.QRect(390, 100, 511, 171))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(40)
        self.chose_text.setFont(font)
        self.chose_text.setAlignment(QtCore.Qt.AlignCenter)
        self.chose_text.setObjectName("chose_text")
        self.btn_back_to_menu = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back_to_menu.setGeometry(QtCore.QRect(20, 30, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily('OCR A Extended')
        self.btn_back_to_menu.setFont(font)
        self.btn_back_to_menu.setText("Back")
        self.btn_back_to_menu.setFlat(True)
        self.btn_back_to_menu.setObjectName("btn_back_to_menu")
        chose_guitar.setCentralWidget(self.centralwidget)

        self.retranslateUi(chose_guitar)
        QtCore.QMetaObject.connectSlotsByName(chose_guitar)

    def retranslateUi(self, chose_guitar):
        _translate = QtCore.QCoreApplication.translate
        chose_guitar.setWindowTitle(_translate("MainWindow", "chose_guitar"))
        self.medium.setText(_translate("MainWindow", "normal"))
        self.hard.setText(_translate("MainWindow", "hard"))
        self.chose_text.setText(_translate("MainWindow", "chose the level"))


