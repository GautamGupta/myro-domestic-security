from myro import *

init("/dev/tty.Fluke2-052F-Fluke2")

picture = takePicture("color")

savePicture(picture, "pic.jpg")
