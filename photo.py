from myro import *
from time import time

class RobotPic:

	# Initiates the picture object, either as nothing or as "picObject"
	def __init__(self, picObject = None):
		self.picture = picObject
		self.table = None

	def genTable(self):
		self.table = [[getRGB(self.picture.getPixel(x,y)) for y in range (getHeight(self.picture))] for x in range(getWidth(self.picture))]

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
			return
		show(self.picture, name)

	# Returns the grayscale version of "self.picture" using averaging algorithm
	def getGrayScale(self):
		if not self.table:
			self.genTable()
		curTime = time()
		if(not self.picture):
			print "No picture to be analyzed"
			return
		width = getWidth(self.picture)
		height = getHeight(self.picture)
		newPic = makePicture(width, height)
		for x in range (width):
			for y in range (height):
				value = sum(self.table[x][y]) / 3
				setPixel(newPic, x, y, makeColor(value, value, value))
		print time() - curTime
		return newPic

	def getSharp(self):
		if not self.table:
			self.genTable()
		curTime = time()
		if(not self.picture):
			print "No picture to be analyzed"
			return
		width = getWidth(self.picture)
		height = getHeight(self.picture)
		newPic = makePicture(width, height)
		matrix = [[-1,0],[0,-1],[1,0],[0,1]]
		margin = 1;
		for x in range (margin, width - margin):
			for y in range (margin, height - margin):
				sumRed = self.table[x][y][0] * (len(matrix) + 1)
				sumGreen = self.table[x][y][1] * (len(matrix) + 1)
				sumBlue = self.table[x][y][2] * (len(matrix) + 1)
				for z in range (len(matrix)):
					sumRed -= self.table[x + matrix[z][0]][y + matrix[z][1]][0]
					sumGreen -= self.table[x + matrix[z][0]][y + matrix[z][1]][1]
					sumBlue -= self.table[x + matrix[z][0]][y + matrix[z][1]][2]
				setPixel(newPic, x, y, makeColor(sumRed, sumGreen, sumBlue))
		print time() - curTime
		return newPic

def run():
	robotPic = RobotPic()
	robotPic.picOpen("pic.jpg")
	robotPic.picShow("Color")
	newPic = RobotPic(robotPic.getGrayScale())
	newPic.picShow("Gray")
	raw_input("Press \"enter\" to quit")
	return

run()