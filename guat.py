from myro import *
from time import time
from photo import RobotPic

# Robot class
class Guatmobile:

    # Logic Variables
    done = 0
    beginTime = 0
    timeElapsed = 0

    # Functions to calculate how long it took to turn at the beginning
    def startTime(self):
        self.beginTime = time()

    def endTime(self):
        self.timeElapsed = time() - self.beginTime
        return self.timeElapsed

    # Delaying functions
    def checkBright(self):
        while self.done == 0:
            if (getLight(0) > 4000000):
                self.startTime()
                beep(1, 880)
                beep(1, 880)
                beep(1, 880)
                self.checkTimer()
        self.done = 0

    # Delaying functions
    def checkTimer(self):
        while self.done == 0:
            if (time() - self.beginTime >= 10):
                beep(3, 880)
                self.done = 1
                self.endTime()