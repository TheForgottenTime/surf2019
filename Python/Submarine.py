
from arduinoSerialCommunicator import writeValue
import time

class Submarine(object):
	"""
		Submarine control class
	"""
	STARTUP_COMMAND_MOTOR0 = "0,59,0"
	def __init__(self):
		sleep(2);
		writeValue(STARTUP_COMMAND_MOTOR0)
		#self.color = color

	def goForward(self, speed):
		writeValue(0 + "," + str(speed) + "," + 0)
		writeValue(1 + "," + str(speed) + "," + 0)
		print("Going forward")

	def goReverse(self, motor, speed):
		writeValue(0 + "," + str(speed) + "," + 1)
		writeValue(1 + "," + str(speed) + "," + 1)
		print("Going backwards")

	def goTurnLeft(self):
		writeValue(0 + "," + str(speed) + "," + 1)
		writeValue(1 + "," + str(speed) + "," + 0)
		sleep(2)
		print("Turning left")

	def goTurnRight(self):
		writeValue(1 + "," + str(speed) + "," + 0)
		writeValue(0 + "," + str(speed) + "," + 1)
		sleep(2)
		print("Turning right")

	def goDown(self):
		writeValue(2 + "," + 45 + "," 0)
		writeValue(3 + "," + 45 + "," 0)
		writeValue(4 + "," + 45 + "," 0)
		writeValue(5 + "," + 45 + "," 0)
		print("Going up")

	def goUp(self):
		writeValue(2 + "," + 135 + "," 0)
		writeValue(3 + "," + 135 + "," 0)
		writeValue(4 + "," + 135 + "," 0)
		writeValue(5 + "," + 135 + "," 0)
		print("Going down")

	def doABarrelRollClockwise(self):
		writeValue(2 + "," + 180 + "," 0)
		writeValue(3 + "," + 1 + "," 0)
		writeValue(4 + "," + 180 + "," 0)
		writeValue(5 + "," + 1 + "," 0)
		print("Doing a barrel roll")
		
	def doABarrelRollCounterClockwise(self):
		writeValue(2 + "," + 1 + "," 0)
		writeValue(3 + "," + 180 + "," 0)
		writeValue(4 + "," + 1 + "," 0)
		writeValue(5 + "," + 180 + "," 0)
		print("Doing a barrel roll")