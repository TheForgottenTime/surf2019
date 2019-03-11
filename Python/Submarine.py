
from arduinoSerialCommunicator import writeValue

class Submarine(object):
	"""
		Submarine control class
	"""
	STARTUP_COMMAND_MOTOR0 = "0,59,0"
	def __init__(self):
		sleep(2);
		writeValue(STARTUP_COMMAND_MOTOR0)
		#self.color = color

	def armHovers(self):
		print("Hover motors armed")

	def armDrivers(self):
		print("Driver motors arrmed")

	def accelarate(self):
		print("accelarating...")
		"accelarator functionality here"

		" gear related functionality here"