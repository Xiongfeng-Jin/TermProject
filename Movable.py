"""
Author: Xiongfeng Jin

this class is for all the object that can move, it set the 
basic move behavior
"""
from Location import *
class Movable(object):
	def __init__(self,location,*args):
		self.location = location
		
	def moveTo(self,x,y):
		'''
		move to a specific x and y that user want go to
		'''
		self.location.setXY(x,y)
		
	def move(self,x=0,y=0):
		'''
		move x and y distance from it original x and y
		'''
		self.location.translateXY(x,y)
		
	def hit(self):
		#to be inplemented
		pass
		
	def getPosition(self):
		'''
		display where it is
		'''
		print("(%s,%s)"%(self.location.x,self.location.y))

if __name__ == '__main__':
	a = Movable(Location(0,1))
	a.getPosition()
	a.move(1244,21)
	a.getPosition()
	a.moveTo(1,2)
	a.getPosition()