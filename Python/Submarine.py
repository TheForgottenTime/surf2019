
from arduinoSerialCommunicator import writeValue
import time

class Submarine(object):
	"""
		Submarine control class
	"""
	def __init__(self):
		writeValue("0,1,0")
		time.sleep(1)
		writeValue("1,1,0")
		print("Startup complete.")
		#self.color = color

	def goForward(self, speed):
		writeValue("0," + str(speed) + ",0")
		time.sleep(1)
		writeValue("1," + str(speed) + ",0")
		print("Going forward")
		time.sleep(1)

	def goReverse(self, speed):
		writeValue("0," + str(speed) + ",1")
		time.sleep(1)
		writeValue("1," + str(speed) + ",1")
		print("Going backwards")
		time.sleep(1)

	def goTurnLeft(self):
		writeValue("0," + "15" + ",1")
		time.sleep(1)
		writeValue("1," + "15" + ",0")
		time.sleep(1)
		print("Turning left")

	def goTurnRight(self):
		writeValue("0," + "15" + ",0")
		time.sleep(1)
		writeValue("1," + "15" + ",1")
		time.sleep(1)
		print("Turning right")

	def goDown(self):
		writeValue("3,180,0")
		print("Going down")

	def goUp(self):
		writeValue("3,0,0")
		print("Going going up")

	def goStop(self):
		writeValue("0,0,0")
		time.sleep(0.8)
		writeValue("1,0,0")
		time.sleep(0.8)
	def doABarrelRollClockwise(self):
		writeValue("2,180,0")
		writeValue("3,1,0")
		writeValue("4,180,0")
		writeValue("5,1,0")
		print("Doing a barrel roll")

	def doABarrelRollCounterClockwise(self):
		writeValue("2,1,0")
		writeValue("3,180,0")
		writeValue("4,1,0")
		writeValue("5,180,0")
		print("Doing a barrel roll")

	def getDepth(self):
		return 10
	
	def getHeading(self):
		return 90
	
	def sweepClockwise(self):
		goTurnRight()
	def sweepCounterClockwise(self):
		goTurnLeft()
	