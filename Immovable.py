"""
Author: Xiongfeng Jin

this class is for the object that can not move,
it will do nothing except telling user the object can not move
when user trying to move something.
"""
from Location import *
class Immovable(Location):
	def __init__(self,x,y):
		super().__init__(x,y)
		
	def moveTo(self,x,y):
		print("I can't move")
		return
		
	def move(self,x,y):
		print("I can't move")
		return
		
	def hit(self):
		#to be inplemented
		pass
		
	def getPosition(self):
		print(self)

if __name__ == '__main__':
	a = Immovable(1,2)
	a.getPosition()
	a.move(1,23)
