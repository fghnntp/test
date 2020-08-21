import minimalmodbus
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from mainWindow import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonStepAngle.clicked.connect(self.show_step_angle)
        self.ui.pushButtonStepInfo.clicked.connect(self.show_step_info)
        self.ui.pushButtonStepDivide.clicked.connect(self.show_step_divided)
        self.ui.pushButtonStepCircleSpeed.clicked.connect(
            self.show_step_circle_speed)
        self.ui.pushButtonStepEnable.clicked.connect(self.show_step_enable)
        self.ui.pushButtonStepBackZero.clicked.connect(
            self.show_step_back_zero)
        self.show()

    def show_step_angle(self):
        """
            show setp motor's step angle
        """
        try:
            step_angle = int(step_motor.read_register(0x0000, 1))
            step_angle = step_angle/100
            self.ui.textEdit.append(str(step_angle))
        except:
            self.ui.textEdit.append('Failed to read from instrument')

    def show_step_info(self):
        """
            show step motor's serial's base information
        """
        try:
            step_info = str(step_motor)
            self.ui.textEdit.append(step_info)
        except:
            self.ui.textEdit.append('Failed to read from instrument')

    def show_step_divided(self):
        """
            show step detailed diveided
        """
        try:
            step_divide = str(step_motor.read_register(0x0001, 1))
            self.ui.textEdit.append(step_divide)
        except:
            self.ui.textEdit.append("Failed to read from instrument.")

    def show_step_circle_speed(self):
        """
            show step motor's circle speed
        """
        try:
            step_circle_speed = str(step_motor.read_register(0x0008, 1))
            self.ui.textEdit.append(step_circle_speed)
        except:
            self.ui.textEdit.append("Failed to read from instrument.")

    def show_step_enable(self):
        """
            show the step motor enable information, 0 is not enable, 
            oppeseely 1 is enable
        """
        try:
            step_enable = str(step_motor.read_register(0x004f, 1))
            self.ui.textEdit.append(step_enable)
        except:
            self.ui.textEdit.append("Failed to read from instrument.")

    def show_step_back_zero(self):
        """
            show the step motor's bact to zero's register's num
        """
        try:
            step_back_zero = str(step_motor.read_register(0x0006, 1))
            self.ui.textEdit.append(step_back_zero)
        except:
            self.ui.textEdit.append("Failed to read from instrument.")


if __name__ == "__main__":
    step_motor = minimalmodbus.Instrument('COM6', 1)
    step_motor.close_port_after_each_call = True
    step_motor.serial.baudrate = 9600

    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())