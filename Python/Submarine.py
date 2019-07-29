
#  from arduinoSerialCommunicator import writeValue
import time
import warnings
import serial
import serial.tools.list_ports


ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600
)


class Submarine(object):
    """
            Submarine control class
    """

    def __init__(self):
        print("Startup complete.")
        # self.color = color

    def goForward(self, speed):
        ser.write('0:130&1:130')
        print("Going forward")

    def goReverse(self, speed):
        ser.write('0:50&1:50')
        print("Going backwards")

    def goSweepLeft(self):
        ser.write('0:130&1:130')
        print("Turning left")

    def goSweepRight(self):
        ser.write('0:130&1:130')
        print("Turning right")

    def goDown(self):
        ser.write('2:30&3:30&4:30&5:30')
        print("Going down")

    def goUp(self):
        ser.write('2:150&3:150&4:150&5:150')
        print("Going up")

    def getDepth(self):
        return 10

    def getHeading(self):
        return 90
