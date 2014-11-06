from myro import *
from time import time
from guat import Guatmobile

# -------------------- Start of Run Sequence ----------------------

# Main function that runs the sequence for the robot
def run():

    # Initialize
    robot = Guatmobile()

    # Loop until the light turns on
    robot.checkBright()
    # Turn back to correct angle

# -------------------- End of Run Sequence ----------------------

# User Control
def main():
    init("/dev/tty.Fluke2-052F-Fluke2")
    finished = 0
    
    while finished == 0:
        select = raw_input("Enter 'r' to run\nEnter 'q' to quit program\n")

        if select == 'r':
            run()

        # Ends the program
        elif select == 'q':
            finished = 1

main()