# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(979, 662)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 280, 431, 211))
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 60, 301, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayoutShowInfo = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayoutShowInfo.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutShowInfo.setObjectName("gridLayoutShowInfo")
        self.pushButtonStepInfo = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonStepInfo.setObjectName("pushButtonStepInfo")
        self.gridLayoutShowInfo.addWidget(self.pushButtonStepInfo, 0, 0, 1, 1)
        self.pushButtonStepBackZero = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonStepBackZero.setObjectName("pushButtonStepBackZero")
        self.gridLayoutShowInfo.addWidget(self.pushButtonStepBackZero, 1, 0, 1, 1)
        self.pushButtonStepCircleSpeed = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonStepCircleSpeed.setObjectName("pushButtonStepCircleSpeed")
        self.gridLayoutShowInfo.addWidget(self.pushButtonStepCircleSpeed, 1, 1, 1, 1)
        self.pushButtonStepEnable = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonStepEnable.setObjectName("pushButtonStepEnable")
        self.gridLayoutShowInfo.addWidget(self.pushButtonStepEnable, 0, 1, 1, 1)
        self.pushButtonClockwise = QtWidgets.QPushButton(Dialog)
        self.pushButtonClockwise.setGeometry(QtCore.QRect(460, 80, 121, 31))
        self.pushButtonClockwise.setObjectName("pushButtonClockwise")
        self.pushButtonAntiClockwise = QtWidgets.QPushButton(Dialog)
        self.pushButtonAntiClockwise.setGeometry(QtCore.QRect(620, 80, 141, 31))
        self.pushButtonAntiClockwise.setObjectName("pushButtonAntiClockwise")
        self.pushButtonStop = QtWidgets.QPushButton(Dialog)
        self.pushButtonStop.setGeometry(QtCore.QRect(460, 140, 93, 28))
        self.pushButtonStop.setObjectName("pushButtonStop")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonStepInfo.setText(_translate("Dialog", "step_info"))
        self.pushButtonStepBackZero.setText(_translate("Dialog", "step_back_zero"))
        self.pushButtonStepCircleSpeed.setText(_translate("Dialog", "step_circle_speed"))
        self.pushButtonStepEnable.setText(_translate("Dialog", "step_enable"))
        self.pushButtonClockwise.setText(_translate("Dialog", "clockwise"))
        self.pushButtonAntiClockwise.setText(_translate("Dialog", "anticlockwise"))
        self.pushButtonStop.setText(_translate("Dialog", "stop"))
