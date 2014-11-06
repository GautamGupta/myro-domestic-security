from myro import *
from time import time

init("/dev/tty.Fluke2-052F-Fluke2")

# Robot class
class Gautmobile:

    # Logic Variables
    done = 0
    beginTime = 0
    turntime = 0

    # Functions to calculate how long it took to turn at the beginning
    def startTime(self):
        self.beginTime = time()

    def endTime(self):
        self.turnTime = time() - self.beginTime
        return self.turnTime

    # Delaying functions
    def checkBright(self):
        while self.done == 0:
            if (getLight(0) > 3000):
                startTime()
                beep(1, 880)
                beep(1, 880)
                beep(1, 880)
                self.done = 1
                checkTimer()
        self.done = 0

    # Delaying functions
    def checkTimer(self):
        while self.done == 0:
            if (time() - self.beginTime >= 120):
                beep(3, 880)
                self.done = 1
                endTime()
        self.done = 0

# -------------------- Start of Run Sequence ----------------------

# Main function that runs the sequence for the robot
def run():

    # Initialize
    robot = Gautmobile()

    # Loop until the light turns on
    robot.checkBright()
    # Turn back to correct angle

# -------------------- End of Run Sequence ----------------------

# User Control
def main():
    finished = 0

    while finished == 0:
    select = raw_input("Enter 'r' to run\nEnter 'q' to quit program\n")

    if select == 'r':
        run()

    # Ends the program
    elif select == 'q':
        finished = 1
