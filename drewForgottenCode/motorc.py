import RPi.GPIO as GPIO
import time

leftMotorPin = 17
rightMotorPin = 27
bottomFrontLeftMotorPin = 29
bottomFrontRightMotorPin = 31
bottomBackLeftMotorPin = 32
bottomBackRightMotorPin = 33

leftDirectionPin = 8
rightDirectionPin = 9

GPIO.setmode(GPIO.BCM)

GPIO.setup(leftMotorPin, GPIO.OUT)
GPIO.setup(rightMotorPin, GPIO.OUT)
GPIO.setup(leftDirectionPin, GPIO.OUT)
GPIO.setup(rightDirectionPin, GPIO.OUT)
GPIO.setup(bottomFrontLeftMotorPin, GPIO.OUT)
GPIO.setup(bottomFrontRightMotorPin, GPIO.OUT)
GPIO.setup(bottomBackLeftMotorPin, GPIO.OUT)
GPIO.setup(bottomBackRightMotorPin, GPIO.OUT)

lm = GPIO.PWM(leftMotorPin, 50) # GPIO 17 for PWM with 50Hz
rm = GPIO.PWM(rightMotorPin, 50)
lmdp = GPIO.PWM(leftDirectionPin, 50)
rmdp = GPIO.PWM(rightDirectionPin, 50)
bflm = GPIO.PWM(bottomFrontLeftMotorPin, 50)
bfrm = GPIO.PWM(bottomFrontRightMotorPin, 50)
bblm = GPIO.PWM(bottomBackLeftMotorPin, 50)
bbrm = GPIO.PWM(bottomBackRightMotorPin, 50)

lm.start(2.5) # Initialization
rm.start(2.5)
bflm.start(2.5)
bfrm.start(2.5)
bblm.start(2.5)
bbrm.start(2.5)
lmdp.start(0)
rmdp.start(0)

def goForward(speed):
    lmdp.ChangeDutyCycle(0)
    rmdp.ChangeDutyCycle(0)
    lm.ChangeDutyCycle(speed)
    rm.ChangeDutyCycle(speed)
    
def goBackwards(speed):
    lmdp.ChangeDutyCycle(10)
    rmdp.ChangeDutyCycle(10)
    lm.ChangeDutyCycle(speed)
    rm.ChangeDutyCycle(speed)
    
def turnLeft(speed):
    lmdp.ChangeDutyCycle(0)
    rmdp.ChangeDutyCycle(10)
    lm.ChangeDutyCycle(speed)
    rm.ChangeDutyCycle(speed)
    
def turnRight(speed):
    lmdp.ChangeDutyCycle(10)
    rmdp.ChangeDutyCycle(0)
    lm.ChangeDutyCycle(speed)
    rm.ChangeDutyCycle(speed)
    
try:
  while True:
    goForward(5)
    time.sleep(0.5)
    goForward(7.5)
    time.sleep(0.5)
    goForward(10)
    time.sleep(0.5)
    goForward(12.5)
    time.sleep(0.5)
    goForward(10)
    time.sleep(0.5)
    goForward(7.5)
    time.sleep(0.5)
    goForward(5)
    time.sleep(0.5)
    goForward(0)
    time.sleep(0.5)
except KeyboardInterrupt:
  lm.stop()
  rm.stop()
  GPIO.cleanup()
