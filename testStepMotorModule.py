from stepMotorModule import StepMotor

import minimalmodbus
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from mainWindow import *


class StepMotorTestClass(QDialog):
    """
        mainwindow to test the stepMotorModule
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.pushButtonClockwise.clicked.connect(self.set_clockwise)
        self.ui.pushButtonAntiClockwise.clicked.connect(self.set_anticlockwise)
        self.ui.pushButtonStop.clicked.connect(self.set_stop)
        self.ui.pushButtonStepInfo.clicked.connect(self.show_step_info)
        self.ui.pushButtonStopBackZero.clicked.connect(self.back_zero)
        self.show()

    def show_step_info(self):
        step_motor_instance.show_step_info()

    def set_clockwise(self):
        step_motor_instance.set_clockwise()

    def set_anticlockwise(self):
        step_motor_instance.set_anticlockwise()

    def set_stop(self):
        step_motor_instance.set_stop()

    def back_zero(self):
        step_motor_instance.set_back_t0_zero()


if __name__ == "__main__":
    step_motor_instance = StepMotor('COM6',back_zero=1, speed=5)
    app = QApplication(sys.argv)
    w = StepMotorTestClass()
    w.show()
    sys.exit(app.exec_())
