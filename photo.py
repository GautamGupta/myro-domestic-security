from myro import *

class RobotPic:

	picture = None

	def picTake(self, type):
		try:
			self.picture = takePicture(type)

		except IOError:
			print "Could not take picture"

		return self

	def picOpen(self, fileName):
		try:
			self.picture = makePicture(fileName)

		except IOError:
			print "Could not find or open file of name", fileName

		return self

	def picSave(self, fileName):
		if(not self.picture):
			print "No picture to be saved"
			return self

		try:
			savePicture(self.picture, fileName)

		except IOError:
			print "Could not save file of name", fileName

		return self

	def picShow(self, name):
		if(not self.picture):
			print "No picture to be shown"
			return self

		show(self.picture, name)

		return self

def run():
	robotPic = RobotPic()
	robotPic.picOpen("pic.jpg")
	robotPic.picShow("Picture")
	return

run()