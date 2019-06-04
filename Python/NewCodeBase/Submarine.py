import time
import threading
import RPi.GPIO as GPIO
from threading import Thread

#The pins on the PI for the motors
lmp = 17 #Left motor pin
rmp = 27 #Right motor pin
ldp = 8 #Left motor direction pin
rdp = 9 #Right motor direction pin

#Init the pins with PWM at 50HZ
lm = GPIO.PWM(lmp, 50)
rm = GPIO.PWM(rmp, 50)
lmd = GPIO.PWM(ldp, 50)
rmd = GPIO.PWM(rdp, 50)

class Submarine(object):

    def __init__(self):
        #threading.Thread.__init__(self)
        #self.pin_stop = threading.Event()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(lmp, GPIO.OUT)
        GPIO.setup(rmp, GPIO.OUT)
        GPIO.setup(ldp, GPIO.OUT)
        GPIO.setup(rdp, GPIO.OUT)
        #self.__thread = threading.Thread(name='ledblink',target=self.__blink_pin)
        #self.__thread.start()

    def goForward(speed):
        lm.ChangeDutyCycle(speed)
        rm.ChangeDutyCycle(speed)
        lmd.ChangeDutyCycle(0)
        rmd.ChangeDutyCycle(0)

    def goBackward(speed):
        lm.ChangeDutyCycle(speed)
        rm.ChangeDutyCycle(speed)
        lmd.ChangeDutyCycle(1)
        rmd.ChangeDutyCycle(1)