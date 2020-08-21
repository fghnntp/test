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
        Dialog.resize(788, 632)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(170, 290, 431, 211))
        self.textEdit.setObjectName("textEdit")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(50, 60, 301, 131))
        self.widget.setObjectName("widget")
        self.gridLayoutShowInfo = QtWidgets.QGridLayout(self.widget)
        self.gridLayoutShowInfo.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutShowInfo.setObjectName("gridLayoutShowInfo")
        self.pushButtonStepInfo = QtWidgets.QPushButton(self.widget)
        self.pushButtonStepInfo.setObjectName("pushButtonStepInfo")
        self.gridLayoutShowInfo.addWidget(self.pushButtonStepInfo, 0, 0, 1, 1)
        self.pushButtonStepDivide = QtWidgets.QPushButton(self.widget)
        self.pushButtonStepDivide.setObjectName("pushButtonStepDivide")
        self.gridLayoutShowInfo.addWidget(self.pushButtonStepDivide, 0, 1, 1, 1)
        self.pushButtonStepBackZero = QtWidgets.QPushButton(self.widget)
        self.pushButtonStepBackZero.setObjectName("pushButtonStepBackZero")
        self.gridLayoutShowInfo.addWidget(self.pushButtonStepBackZero, 1, 0, 1, 1)
        self.pushButtonStepCircleSpeed = QtWidgets.QPushButton(self.widget)
        self.pushButtonStepCircleSpeed.setObjectName("pushButtonStepCircleSpeed")
        self.gridLayoutShowInfo.addWidget(self.pushButtonStepCircleSpeed, 1, 1, 1, 1)
        self.pushButtonStepEnable = QtWidgets.QPushButton(self.widget)
        self.pushButtonStepEnable.setObjectName("pushButtonStepEnable")
        self.gridLayoutShowInfo.addWidget(self.pushButtonStepEnable, 2, 0, 1, 1)
        self.pushButtonStepAngle = QtWidgets.QPushButton(self.widget)
        self.pushButtonStepAngle.setObjectName("pushButtonStepAngle")
        self.gridLayoutShowInfo.addWidget(self.pushButtonStepAngle, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonStepInfo.setText(_translate("Dialog", "step_info"))
        self.pushButtonStepDivide.setText(_translate("Dialog", "step_divide"))
        self.pushButtonStepBackZero.setText(_translate("Dialog", "step_back_zero"))
        self.pushButtonStepCircleSpeed.setText(_translate("Dialog", "step_circle_speed"))
        self.pushButtonStepEnable.setText(_translate("Dialog", "step_enable"))
        self.pushButtonStepAngle.setText(_translate("Dialog", "setp angle"))
