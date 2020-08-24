# This is the distutils script for creating a Python-based com (exe or dll)
# server using win32com.  This script should be run like this:
#
#  % python setup.py py2exe
#
# After you run this (from this directory) you will find two directories here:
# "build" and "dist".  The .dll or .exe in dist is what you are looking for.
##############################################################################

from distutils.core import setup
import py2exe
import sys
import minimalmodbus

class StepMotor(minimalmodbus.Instrument):
    """

        input args ...
        port: the COM of the serial, like 'COM1'
        slave_address: The valid slave address range for normal usage is 1 to 247,
                       here, mostly be given in 1
        divided: the detail divided of step controller, 
                 must in {1, 2, 4, 8}, mostly should be 1
        back_zero: the external channel for mechanical zero singal, 
                   must in {0, 1, 2, 3, 4, 5}, 0 means no singal
        speed: the speed of step motor rotate,
               must in [1-9](interger must be given)

    """
    def __init__(self, port, slave_address=1, divided=1, back_zero=0, speed=2):
        super().__init__(port, slave_address)
        self.serial.baudrate = 9600
        self.close_port_after_each_call = True
        self.divide = divided
        self.back_zero = back_zero
        self.speed = speed
        self.set_divide()
        self.set_step_back_zero()
        self.set_step_circle_speed()
        
        
    def show_step_info(self):
        """
            show step motor's serial's base information
        """
        for _ in range(10):
            try:
                step_info = str(self)
                print(step_info)
            except:
                pass
            else:
                print('read from instrument successfully')
                break
        else:
            print("can't read from instrument")

    def set_divide(self):
        """
            set the step motor step detail divide
        """
        # try to read the divided num
        for _ in range(10):
            if self.divide in {1, 2, 4, 8}:
                try:
                    while(int(self.read_register(0x0001, 1)) != self.divide):
                        self.write_register(0x0001, self.divide, 1)
                except:
                    pass
                else:
                    print('set successfully')
                    break
        else:
            print("can't set the divided")

    def set_step_back_zero(self):
        """
            set the step motor's back to zero's register's num, i.e, the channel
        """
        for _ in range(10): 
            if self.back_zero in {0, 1, 2, 3, 4, 5}:
                try:
                    while(int(self.read_register(0x0006, 1)) != self.back_zero):
                        self.write_register(0x0006, self.back_zero, 1)
                except:
                    pass
                else:
                    print('set back to zero successfully')
                    break
        else:
            print("can't set the back to zero")

    def set_step_circle_speed(self):
        """
            set step motor's circle speed
        """
        for _ in range(10):
            if self.speed > 0 and self.speed < 10:
                try:
                    while(int(self.read_register(0x0008, 1)) != self.speed):
                        self.write_register(0x0008, self.speed, 1)
                except:
                    pass
                else:
                    print('set speed successfully')
                    break
        else:
            print("can't set the speed")

    def set_clockwise(self):
        """
            set the step motor clockwise rotate
        """
        for _ in range(10):
            try:
                self.write_bit(0x0003, 0)
                self.write_bit(0x0005, 0)
                self.write_bit(0x0004, 1)
            except:
                pass
            else:
                print('set_clockwise successfully')
                break
        else:
            print("can't set_clockwise")
        
    def set_anticlockwise(self):
        """
            set the step motor anticlockwise rotate
        """
        for _ in range(10):
            try:
                self.write_bit(0x0003, 0)
                self.write_bit(0x0004, 0)
                self.write_bit(0x0005, 1)    
            except:
                pass
            else:
                print("set anticlockwise successfully.")
                break
        else:
            print("can't set anticlockwise")

    def set_stop(self):
        """
            let the step motor stop
        """
        for _ in range(10):
            try:
                self.write_bit(0x0004, 0)
                self.write_bit(0x0005, 0)
                self.write_bit(0x0009, 0)
                self.write_bit(0x0003, 1)
            except:
                pass
            else:
                print("stop the step motor successfully.")
                break
        else:
            print("can't stop the step motor")

    def set_back_t0_zero(self):
        """
            back to zero
        """
        for _ in range(10):
            flag = self.back_zero
            if flag != 0:
                try:
                    self.write_bit(0x0003, 0)
                    self.write_bit(0x0004, 0)
                    self.write_bit(0x0005, 0)
                    self.write_bit(0x0009, 1)
                except:
                    pass
                else:
                    print("back zero successfully.")
                    break
        else:
            print("can't set back to zero")


