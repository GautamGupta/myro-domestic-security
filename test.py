from myro import *
from time import *
from guat import Guatmobile
from photo import RobotPic
import urllib2
import ast

# -------------------- Start of Run Sequence ----------------------

# Main function that runs the sequence for the robot
def run():

    done = False
    
    while not done:
        if(getObstacle('center') > 0):
            request = urllib2.Request("http://myro-robot.appspot.com/?key=6969")
            response = urllib2.urlopen(request)
            html = response.read()
            html = ast.literal_eval(html)
            print html
            request = urllib2.Request("http://myro-robot.appspot.com/2?check=1")
            response = urllib2.urlopen(request)
            html = response.read()
            html = ast.literal_eval(html)
            print html
            request = urllib2.Request("http://myro-robot.appspot.com/2?check=0")
            response = urllib2.urlopen(request)
            html = response.read()
            html = ast.literal_eval(html)
            print html
            """sleep(2)
            speak("Taking Picture")
            robotPic = RobotPic()
            robotPic.picTake("gray")
            #speak("Took Picture")
            robotPic = RobotPic(robotPic.filterGray(100, 100))
            robotPic.picShow("Gray")
            #speak("Filtered Picture")
            robotPic.findSquares(120, 20, 10)
            #speak("Searched For Squares")
            robotPic.gridShow()
            code = robotPic.getCode(3)
            print html
            print code"""

            done = True

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