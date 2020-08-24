import minimalmodbus
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from mainWindow import *


class StepMotorSer(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonDivide.clicked.connect(self.set_divide)
        self.ui.pushButtonStepBackZero.clicked.connect(
            self.set_step_back_zero)
        self.ui.pushButtonStepCircleSpeed.clicked.connect(
            self.set_step_circle_speed)
        self.ui.pushButtonClockwise.clicked.connect(self.set_clockwise)
        self.ui.pushButtonAntiClockwise.clicked.connect(self.set_anticlockwise)
        self.ui.pushButtonStop.clicked.connect(self.set_stop)
        self.ui.pushButtonStepInfo.clicked.connect(self.show_step_info)
        self.show()

    def set_divide(self):
        """
            set the step motor step detail divide
        """
        # try to read the divided num
        count = 5
        while(count > 0):
            count -= 1
            try:
                num = self.ui.lineEditStepSpeedDivide.text()
                num = int(num)
            except:
                self.ui.textEdit.append('Please set divide')
            # if the divided num is right, try to set the divided num
            if num in {1, 2, 4, 8}:
                try:
                    while(int(step_motor.read_register(0x0001, 1)) != num):
                        step_motor.write_register(0x0001, num, 1)
                except:
                    self.ui.textEdit.append('wrong set')
                else:
                    self.ui.textEdit.append('set successfully')
                    break
            else:
                self.ui.textEdit.append(
                    'Please input the right num in {1, 2, 4, 8}')

    def set_step_back_zero(self):
        """
            set the step motor's back to zero's register's num, i.e, the channel 
        """
        # try to read the back zero num
        count = 5
        while(count > 0):
            count -= 1
            try:
                num = self.ui.lineEditBackZero.text()
                num = int(num)
            except:
                self.ui.textEdit.append('Please set back_zero')
            # if the divided num is right, try to set the step_back_zero num
            if num in {0, 1, 2, 3, 4, 5}:
                try:
                    while(int(step_motor.read_register(0x0006, 1)) != num):
                        step_motor.write_register(0x0006, num, 1)
                except:
                    self.ui.textEdit.append('wrong set')
                else:
                    self.ui.textEdit.append('set successfully')
                    break
            else:
                self.ui.textEdit.append(
                    'Please input the right num in {0, 1, 2, 3, 4, 5}')

    def set_step_circle_speed(self):
        """
            set step motor's circle speed
        """
        count = 5
        while(count > 0):
            count -= 1
            # try to read the step motor speed num
            try:
                num = self.ui.lineEditStepSpeed.text()
                num = int(num)
            except:
                self.ui.textEdit.append('Please set step_circle_speed')
            # if the step motor speed num is right, try to set the motor speed num
            if num > 0 and num < 10:
                try:
                    while(int(step_motor.read_register(0x0008, 1)) != num):
                        step_motor.write_register(0x0008, num, 1)
                except:
                    self.ui.textEdit.append('wrong set')
                else:
                    self.ui.textEdit.append('set successfully')
                    break
            else:
                self.ui.textEdit.append(
                    'Please input the right num, 0 < num < 10 ')

    def set_clockwise(self):
        """
            set the step motor clockwise rotate
        """
        count = 5
        while(count > 0):
            count -= 1
            try:
                step_motor.write_bit(0x0005, 0)
                step_motor.write_bit(0x0004, 1)
            except:
                self.ui.textEdit.append("Failed to write in 0x0004.")
            else:
                self.ui.textEdit.append('write in 0x0004 successfully')
                break

    def set_anticlockwise(self):
        """
            set the step motor anticlockwise rotate
        """
        count = 5
        while(count > 0):
            count -= 1
            try:
                step_motor.write_bit(0x0004, 0)
                step_motor.write_bit(0x0005, 1)
            except:
                self.ui.textEdit.append("Failed to write in 0x0005.")
            else:
                self.ui.textEdit.append("write in 0x0005 successfully.")
                break

    def set_stop(self):
        """
            let the step motor stop
        """
        count = 5
        while(count > 0):
            count -= 1
            try:
                step_motor.write_bit(0x0004, 0)
                step_motor.write_bit(0x0005, 0)
            except:
                self.ui.textEdit.append("Failed to stop the step_motor.")
            else:
                self.ui.textEdit.append("stop the step_motor successfully.")
                break

    def show_step_info(self):
        """
            show step motor's serial's base information
        """
        count = 5
        while(count > 0):
            count -= 1
            try:
                step_info = str(self.step_motor)
                self.ui.textEdit.append(step_info)
            except:
                self.ui.textEdit.append('Failed to read from instrument')
            else:
                self.ui.textEdit.append('read from instrument successfully')


if __name__ == "__main__":
    # set up serial's infomation`
    step_motor = minimalmodbus.Instrument('COM6', 1)
    step_motor.close_port_after_each_call = True
    step_motor.serial.baudrate = 9600

    app = QApplication(sys.argv)
    w = StepMotorSer()
    w.show()
    sys.exit(app.exec_())
