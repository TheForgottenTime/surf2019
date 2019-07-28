import time
import serial

ser = serial.Serial(
    port='COM5',
    baudrate=9600
)
while 1:
    inp = input("<< ")
    ser.write(inp.encode())
    time.sleep(.5)
    out = ''
    
    while 1:
        if ser.inWaiting() > 0:
            out = ser.readline()
            if out != '':
               print(">>" + out.decode())
            if out.decode() == 'OK\r\n':
                break
