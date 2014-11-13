from myro import *
from time import time
from guat import Guatmobile
from photo import RobotPic

# -------------------- Start of Run Sequence ----------------------

# Main function that runs the sequence for the robot
def run():

    robotPic = RobotPic()
    robotPic.picTake("gray")
    robotPic.picShow("Gray")
    robotPic = RobotPic(robotPic.filterGray(100, 100))
    robotPic.picShow("Filtered")
    pattern = RobotPic(robotPic.findSquares(120, 20, 10))
    pattern.picShow("Pattern")
    print pattern.getCode(3)

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