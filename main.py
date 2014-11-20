from myro import *
from time import *
from guat import Guatmobile
from photo import RobotPic

# -------------------- Start of Run Sequence ----------------------

# Main function that runs the sequence for the robot
def run():
    state = 0
    while state != -1:         
        if state == 0:
            select = raw_input("Choose from the following:\n(a) - Arm the alarm\n(q) - Quit the program\n")
            if select == 'a':
                speak("Alarm armed")
                state = 1
            elif select == 'q':
                state = -1
        elif state == 1:        
            robot = Guatmobile()
            if robot.checkBright():
                state = 0
                speak("Alarm disarmed")
            else:
                state = 2
        elif state == 2:
            robot.intruder()
            state = 0

    
# -------------------- End of Run Sequence ----------------------

# User Control
def main():
    init("/dev/tty.Fluke2-052F-Fluke2")
    run()

main()