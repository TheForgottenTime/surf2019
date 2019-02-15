# This allows for the communication between python running on the Pi
# and the arudino.
# Runs on Python 3.X
# Open arduino and find the board port then fill that in for variable port below
# make sure arduino serial monitor isn't open while this is running
import threading
import time
import serial

ser = serial.Serial(
    port='/dev/cu.usbmodem142101',
    baudrate=9600,
)
if ser.isOpen():
    ser.close()
ser.open()
ser.isOpen()

time.sleep(2)
ser.write(b'0,100,255')

def readSerial():
    while True:
        ser_bytes = ser.readline()
        print(ser_bytes)

def writeSerial():
    while True:
        com = input('Command:')
        ser.write(str.encode(com))

threading.Thread(target=readSerial()).start()
#threading.Thread(target=writeSerial()).start()
