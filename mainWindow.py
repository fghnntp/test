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
        Dialog.resize(857, 641)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(180, 360, 431, 211))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 30, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 110, 631, 65))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonDivide = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonDivide.setObjectName("pushButtonDivide")
        self.gridLayout.addWidget(self.pushButtonDivide, 0, 2, 1, 1)
        self.lineEditStepSpeedDivide = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditStepSpeedDivide.setObjectName("lineEditStepSpeedDivide")
        self.gridLayout.addWidget(self.lineEditStepSpeedDivide, 0, 3, 1, 1)
        self.pushButtonStepBackZero = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonStepBackZero.setObjectName("pushButtonStepBackZero")
        self.gridLayout.addWidget(self.pushButtonStepBackZero, 1, 0, 1, 1)
        self.lineEditBackZero = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditBackZero.setObjectName("lineEditBackZero")
        self.gridLayout.addWidget(self.lineEditBackZero, 1, 1, 1, 1)
        self.pushButtonStepCircleSpeed = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonStepCircleSpeed.setObjectName("pushButtonStepCircleSpeed")
        self.gridLayout.addWidget(self.pushButtonStepCircleSpeed, 1, 2, 1, 1)
        self.lineEditStepSpeed = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditStepSpeed.setObjectName("lineEditStepSpeed")
        self.gridLayout.addWidget(self.lineEditStepSpeed, 1, 3, 1, 1)
        self.pushButtonStepInfo = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonStepInfo.setObjectName("pushButtonStepInfo")
        self.gridLayout.addWidget(self.pushButtonStepInfo, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 230, 401, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonClockwise = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonClockwise.setObjectName("pushButtonClockwise")
        self.gridLayout_2.addWidget(self.pushButtonClockwise, 0, 0, 1, 1)
        self.pushButtonAntiClockwise = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonAntiClockwise.setObjectName("pushButtonAntiClockwise")
        self.gridLayout_2.addWidget(self.pushButtonAntiClockwise, 0, 1, 1, 1)
        self.pushButtonStop = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.gridLayout_2.addWidget(self.pushButtonStop, 1, 0, 1, 1)
        self.pushButtonStopBackZero = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonStopBackZero.setObjectName("pushButtonStopBackZero")
        self.gridLayout_2.addWidget(self.pushButtonStopBackZero, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Step Motor Debuggint Pannel"))
        self.pushButtonDivide.setText(_translate("Dialog", "step_divide"))
        self.pushButtonStepBackZero.setText(_translate("Dialog", "step_back_zero"))
        self.pushButtonStepCircleSpeed.setText(_translate("Dialog", "step_circle_speed"))
        self.pushButtonStepInfo.setText(_translate("Dialog", "step_info"))
        self.pushButtonClockwise.setText(_translate("Dialog", "clockwise"))
        self.pushButtonAntiClockwise.setText(_translate("Dialog", "anticlockwise"))
        self.pushButtonStop.setText(_translate("Dialog", "stop"))
        self.pushButtonStopBackZero.setText(_translate("Dialog", "back_zero"))
