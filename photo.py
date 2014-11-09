from myro import *

class RobotPic:

	# Initiates the picture object, either as nothing or as "picObject"
	def __init__(self, picObject = None):
		self.picture = picObject

	# Uses the "takePicure" Myro function to take a picture and store it at variable "self.picture"
	def picTake(self, type):
		try:
			self.picture = takePicture(type)
		except IOError:
			print "Could not take picture"

	# Opens a picture from "fileName" and stores it at variable "self.picture"
	def picOpen(self, fileName):
		try:
			self.picture = makePicture(fileName)
		except IOError:
			print "Could not find or open file of name", fileName

	# Saves "self.picture" in the same folder as the py file under the name "fileName"
	def picSave(self, fileName):
		if(not self.picture):
			print "No picture to be saved"
			return
		try:
			savePicture(self.picture, fileName)
		except IOError:
			print "Could not save file of name", fileName

	# Uses the Myro "show" function to display "self.picture" in a new windows under the name "name"
	def picShow(self, name):
		if(not self.picture):
			print "No picture to be shown"
		show(self.picture, name)

	# Returns the grayscale version of "self.picture" using averaging algorithm
	def getGrayScale(self):
		if(not self.picture):
			print "No picture to be analyzed"
		width = getWidth(self.picture)
		height = getHeight(self.picture)
		newPic = makePicture(width, height)
		for x in range (width):
			for y in range (height):
				value = sum(getRGB(self.picture.getPixel(x, y))) / 3
				setPixel(newPic, x, y, makeColor(value, value, value))
		return newPic

def run():
	robotPic = RobotPic()
	robotPic.picOpen("pic.jpg")
	robotPic.picShow("Color")
	newRobotPic = RobotPic(robotPic.getGrayScale())
	newRobotPic.picShow("GrayScale")
	raw_input("Press \"enter\" to quit")
	return

run()
