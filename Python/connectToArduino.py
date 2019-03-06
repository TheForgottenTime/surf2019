import warnings
import serial
import serial.tools.list_ports

baud = 9600

def getSerialPort():
    arduino_ports = [
        p.device
        for p in serial.tools.list_ports.comports()
        if 'Arduino' in p.description or 'CDC' in p.description 
    ]
    if not arduino_ports:
        raise IOError("No Arduino found")
    if len(arduino_ports) > 1:
        warnings.warn('Multiple Arduinos found - using the first')

    ser = serial.Serial(arduino_ports[0], baud, timeout=0)
    return ser

