from Submarine import Submarine
import time
import threading

thisSub = Submarine()
time.sleep(3)
thisSub.goForward(20)
time.sleep(6)
thisSub.goReverse(20)
time.sleep(3)

