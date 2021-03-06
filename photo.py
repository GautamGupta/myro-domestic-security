from myro import *
from time import time

class RobotPic:

	# Initiates the picture object, either as nothing or as "picObject"
	def __init__(self, picObject = None):
		self.picture = picObject
		self.table = None
		self.grid = None

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
		if not self.picture:
			print "No picture to be saved"
			return
		try:
			savePicture(self.picture, fileName)
		except IOError:
			print "Could not save file of name", fileName

	# Uses the Myro "show" function to display "self.picture" in a new windows under the name "name"
	def picShow(self, name):
		if not self.picture:
			print "No picture to be shown"
			return
		show(self.picture, name)

	# Returns the grayscale version of "self.picture" using averaging algorithm
	def getGrayScale(self):
		if not self.picture:
			print "No picture to be shown"
			return
		if not self.table:
			self.genTable()
		width = getWidth(self.picture)
		height = getHeight(self.picture)
		newPic = makePicture(width, height)
		for x in range (width):
			for y in range (height):
				value = sum(self.table[x][y]) / 3
				setPixel(newPic, x, y, makeColor(value, value, value))
		return newPic

	def getSharp(self):
		if not self.picture:
			print "No picture to be shown"
			return
		if not self.table:
			self.genTable()
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
		return newPic

	def filterGray(self, value, threshold, color = makeColor(0, 255, 0)):
		if not self.picture:
			print "No picture to be shown"
			return
		if not self.table:
			self.genTable()
		width = getWidth(self.picture)
		height = getHeight(self.picture)
		newPic = makePicture(width, height)
		for x in range (width):
			for y in range (height):
				if value < sum(self.table[x][y]) / 3 + threshold and value > sum(self.table[x][y]) / 3 - threshold:
					setPixel(newPic, x, y, color)
		return newPic

	def findSquares(self, size, threshold, interval, color = makeColor(0, 255, 0)):
		if not self.picture:
			print "No picture to be shown"
			return
		if not self.table:
			self.genTable()
		squares = []
		width = getWidth(self.picture)
		height = getHeight(self.picture)
		y = size / 2
		while y < height - size / 2:
			x = 0
			while x < width - size:
				if sum(self.table[x][y]) != 255 * 3:
					incr = -1
					bounds = [x + size / 2, y, x + size / 2, y]
					newBounds = bounds
					for i in range (4):
						bounds = [x + size / 2, y, x + size / 2, y]
						if i > 1:
							incr = 1
						while sum(self.table[bounds[incr + 1]][bounds[incr + 2]]) != 255 * 3:
							if bounds[incr + 1] > 0 and bounds[incr + 1] < width - 1 and bounds[incr + 2] > 0 and bounds[incr + 2] < height - 1:
								bounds[i] += incr
								newBounds[i] += incr
							else:
								break
					newWidth = newBounds[2] - newBounds[0]
					newHeight = newBounds[3] - newBounds[1]
					if newHeight > size - threshold and newHeight < size + threshold and newWidth > size - threshold and newWidth < size + threshold:
						squares.append(newBounds)
					x = newBounds[2]
				x += 1
			y += interval
		if not squares:
			print "Did not find squares"
			return None
		picBounds = [width, height, 0, 0]
		for square in squares:
			if picBounds[0] > square[0]:
				picBounds[0] = square[0]
			if picBounds[1] > square[1]:
				picBounds[1] = square[1]
			if picBounds[2] < square[2]:
				picBounds[2] = square[2]
			if picBounds[3] < square[3]:
				picBounds[3] = square[3]
		matrix = [[0 for y in range(picBounds[3] - picBounds[1])] for y in range(picBounds[2] - picBounds[0])]
		for square in squares:
			for x in range(picBounds[2] - picBounds[0]):
				for y in range(picBounds[3] - picBounds[1]):
					if x >= square[0] - picBounds[0] and x <= square[2] - picBounds[0] and y >= square[1] - picBounds[1] and y <= square[3] - picBounds[1]:
						matrix[x][y] = 1;
		self.grid = matrix
		return matrix
		"""newPic = makePicture(picBounds[2] - picBounds[0], picBounds[3] - picBounds[1])
		for x in range(picBounds[2] - picBounds[0]):
			for y in range(picBounds[3] - picBounds[1]):
				if matrix[x][y]:
					setPixel(newPic, x, y, color)
		return newPic"""

	def getCode(self, size):
		"""if not self.picture:
			print "No picture to be shown"
			return"""
		if not self.grid:
			print "No grid exists"
			return
		"""width = getWidth(self.picture)
		height = getHeight(self.picture)"""
		width = len(self.grid)
		height = len(self.grid[0])
		print width
		print height
		interval_x = width / size
		interval_y = height / size
		matrix = [0 for i in range(size * size)]
		y = interval_y / 2
		i = 0
		while y < height:
			x = interval_x / 2
			j = 0
			while x < width:
				if self.grid[x][y]:
					matrix[i * size + j] = 1
				x += interval_x
				j += 1
			y += interval_y
			i += 1
		return matrix

	def gridShow(self, color = makeColor(0, 255, 0)):
		if not self.grid:
			print "No grid exists"
			return
		newPic = makePicture(len(self.grid), len(self.grid[0]))
		for x in range(len(self.grid)):
			for y in range(len(self.grid[0])):
				if self.grid[x][y]:
					setPixel(newPic, x, y, color)
		show(newPic)

def run():
    robotPic = RobotPic()
    robotPic.picOpen("pic.jpg")
    newPic = RobotPic(robotPic.filterGray(205, 50))
    pattern = RobotPic(newPic.findSquares(130, 30, 10))
    pattern.picShow("Pattern")
    print pattern.getCode(3)
    raw_input("Press \"enter\" to quit")
    return

# run()