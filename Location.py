"""
Author: Xiongfeng Jin

this is the super class for all the object on the screen,
it specify where the object on the screen and set the basic 
move behavior
"""
from math import sqrt, pi, cos, sin

def distance(loc1, loc2):
    '''Computes the distance between two Locations'''
    return sqrt((loc1.x-loc2.x)**2+(loc1.y-loc2.y)**2)

 
class Location():
	def __init__(self,x,y):
		'''
		initialize x and y
		'''
		self.x = x
		self.y = y
		
	def setX(self,x):
		'''
		set x
		'''
		self.x = x
		
	def setY(self,y):
		'''
		set y
		'''
		self.y = y
		
	def setXY(self,x,y):
		'''
		set x and y
		'''
		self.x = x
		self.y = y
		
	def translateXY(self,x,y):
		'''
		to add a new x and y to the old x and y
		'''
		self.x += x
		self.y += y
		
	def translateHM(self,x,y):
		#implement after
		pass
		
	def getX(self):
		'''
		to see the x
		'''
		return self.x
		
	def getY(self):
		'''
		to see the y
		'''
		return self.y
		
	def clone(self):
		'''
		to make a instance with same location
		'''
		return Location(self.x,self.y)
		
	def __str__(self):
		'''
		to see the x and y
		'''
		return "("+str(self.x)+","+str(self.y)+")"