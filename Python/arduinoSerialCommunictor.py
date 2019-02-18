# This allows for the communication between python running on the Pi
# and the arudino.
# Runs on Python 3.X
# Open arduino and find the board port then fill that in for variable port below
# make sure arduino serial monitor isn't open while this is running
import threading
import time
import serial

from random import randint

port = '/dev/cu.usbmodem144101'
baud = 9600

serial_port = serial.Serial(port, baud, timeout=0)

def handle_data(data):
    print(data)

def read_from_port(ser):

    while True:
        reading = ser.readline().decode()
        if(len(reading) != 0):
            handle_data(reading)
'''            
def write_to_port(ser,value):
    while True:
        rand = randint(0,100)
        writingString = '0,'+ str(rand) + ',255'
        ser.write(str.encode(writingString))
        time.sleep(2)
'''       
def writeValue(value):
    serial_port.write(str.encode(value))
    
thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()
time.sleep(2)
writeValue("0,90,255")

#threading.Thread(target=writeSerial()).start()
