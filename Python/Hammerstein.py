# Python programme for controlling Arduino Nano connected to a Raspberry Pi using i2c serial communication
# inspiration for the i2c element from Oscar laing's Blog
# http://blog.oscarliang.net/raspberry-pi-arduino-connected-i2c
# Commands sent to Raspberry Pi over a web page using webiopi
# Prior to running this program you must start the pigpio daemon if using the Pi GPIO
# by either entering pigpiod at a command prompt or running it automatically at startup
# as a CRON job
# If you recieve a module import error no module named smbus ensure version of smbus
# and WebIOPi Python match

# /usr/bin/env python

import webiopi 	# Import webiopi - software to communicate with a Rapsberry Pi over a web interface
import smbus as smbus
import time
import os  # used to call bash sripts

# Uncomment the following two lines if using the Pi GPIO
# import pigpio # pigpio is a custom module for controlling GPIO pins
# pi = pigpio.pi #declare psuedo for pigpio commands

bus = smbus.SMBus(1)  # For RPI version 1 use "bus = smbus.SMBus(0)"

# Setup i2C communication address (must be the same as address set on Arduino
address = 0x04


def writeNumber(value):
    # bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    ser.write(inp.encode())
    return -1


def readNumber():
    number = bus.read_byte_data(address, 1)
    return number

# @webiopi.macro


def stop():
    number = 0
    writeNumber(number)
    time.sleep(1)

# @webiopi.macro


def forward():
    number = 1
    writeNumber(number)
    time.sleep(1)

# @webiopi.macro


def left():
    number = 2
    writeNumber(number)
    time.sleep(1)

# @webiopi.macro


def right():
    number = 3
    writeNumber(number)
    time.sleep(1)

# @webiopi.macro


def backward():
    number = 4
    writeNumber(number)
    time.sleep(1)

# @webiopi.macro


def servo_centre():
    number = 5
    writeNumber(number)
    time.sleep(1)

# @webiopi.macro


def servo_left():
    number = 6
    writeNumber(number)
    time.sleep(1)

# @webiopi.macro


def servo_right():
    number = 7
    writeNumber(number)
    time.sleep(1)

# @webiopi.macro


def led_on():
    number = 8
    writeNumber(number)
    time.sleep(1)

# @webiopi.macro


def led_off():
    number = 9
    writeNumber(number)
    time.sleep(1)


# Start the webiopi server
server = webiopi.Server(port=8000, login="Hammerstein", password="Hammerstein")

# Start the webcam video stream
# os.system("streamer.sh")

# Register the macros
server.addMacro(stop)
server.addMacro(forward)
server.addMacro(left)
server.addMacro(right)
server.addMacro(backward)
server.addMacro(stop)
server.addMacro(servo_centre)
server.addMacro(servo_left)
server.addMacro(servo_right)
server.addMacro(led_on)
server.addMacro(led_off)

# Run default loop

webiopi.runLoop()

# Cleanly stop the server
server.stop()
