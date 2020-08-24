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
        self.textEdit.setGeometry(QtCore.QRect(170, 360, 431, 211))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 30, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(90, 110, 631, 65))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonDivide = QtWidgets.QPushButton(self.widget)
        self.pushButtonDivide.setObjectName("pushButtonDivide")
        self.gridLayout.addWidget(self.pushButtonDivide, 0, 2, 1, 1)
        self.lineEditStepSpeedDivide = QtWidgets.QLineEdit(self.widget)
        self.lineEditStepSpeedDivide.setObjectName("lineEditStepSpeedDivide")
        self.gridLayout.addWidget(self.lineEditStepSpeedDivide, 0, 3, 1, 1)
        self.pushButtonStepBackZero = QtWidgets.QPushButton(self.widget)
        self.pushButtonStepBackZero.setObjectName("pushButtonStepBackZero")
        self.gridLayout.addWidget(self.pushButtonStepBackZero, 1, 0, 1, 1)
        self.lineEditBackZero = QtWidgets.QLineEdit(self.widget)
        self.lineEditBackZero.setObjectName("lineEditBackZero")
        self.gridLayout.addWidget(self.lineEditBackZero, 1, 1, 1, 1)
        self.pushButtonStepCircleSpeed = QtWidgets.QPushButton(self.widget)
        self.pushButtonStepCircleSpeed.setObjectName("pushButtonStepCircleSpeed")
        self.gridLayout.addWidget(self.pushButtonStepCircleSpeed, 1, 2, 1, 1)
        self.lineEditStepSpeed = QtWidgets.QLineEdit(self.widget)
        self.lineEditStepSpeed.setObjectName("lineEditStepSpeed")
        self.gridLayout.addWidget(self.lineEditStepSpeed, 1, 3, 1, 1)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(190, 230, 401, 71))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonClockwise = QtWidgets.QPushButton(self.widget1)
        self.pushButtonClockwise.setObjectName("pushButtonClockwise")
        self.gridLayout_2.addWidget(self.pushButtonClockwise, 0, 0, 1, 1)
        self.pushButtonAntiClockwise = QtWidgets.QPushButton(self.widget1)
        self.pushButtonAntiClockwise.setObjectName("pushButtonAntiClockwise")
        self.gridLayout_2.addWidget(self.pushButtonAntiClockwise, 0, 1, 1, 1)
        self.pushButtonStop = QtWidgets.QPushButton(self.widget1)
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.gridLayout_2.addWidget(self.pushButtonStop, 1, 0, 1, 1)
        self.pushButtonStepInfo = QtWidgets.QPushButton(self.widget1)
        self.pushButtonStepInfo.setObjectName("pushButtonStepInfo")
        self.gridLayout_2.addWidget(self.pushButtonStepInfo, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Step Motor Debuggint Pannel"))
        self.pushButtonDivide.setText(_translate("Dialog", "step_divide"))
        self.pushButtonStepBackZero.setText(_translate("Dialog", "step_back_zero"))
        self.pushButtonStepCircleSpeed.setText(_translate("Dialog", "step_circle_speed"))
        self.pushButtonClockwise.setText(_translate("Dialog", "clockwise"))
        self.pushButtonAntiClockwise.setText(_translate("Dialog", "anticlockwise"))
        self.pushButtonStop.setText(_translate("Dialog", "stop"))
        self.pushButtonStepInfo.setText(_translate("Dialog", "step_info"))
