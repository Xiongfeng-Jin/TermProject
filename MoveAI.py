"""
Author: Xiongfeng Jin

This is the basic move behavior for all the alive object,
it defines all kinds of movement.
"""
from Movable import *
from Immovable import *
from random import random, randint


class RandomWalk():
	def __init__(self,simobj,lrx = 0,lry =0,hrx = None,hry = None):
		'''
		random move Ai, makes an object move randomly
		'''
		self.simobj = simobj
		self.rx = randint(0,1)
		self.ry = randint(0,1)
		self.lrx = lrx
		self.lry = lry
		self.hrx = hrx
		self.hry = hry
		self.step = 0.1
	def move(self):
		'''
		randomly move an object, for free npcs and animals
		and some other objects that has no walkinng purpose
		it restrict the object move outside the map, which means
		object"x and y will not smaller than 0.
		args:
			lrx: low restrict of x, object"x may not lower than lrx
			lry: low restrict of y, object"y may not lower than lry
			hrx: high restrict of x, object"x may not higher than hrx
			hry: high restrict of y, object"y may not higher than hry
			ex. if lrx = 10, lry = 10, hrx = 20, hry = 20
			then object will only move in the area between (10,10) and (20,20)
			which means the object"x is from 10 to 20, and y is from 10 to 20
		'''
		if self.simobj.location.x <= self.lrx and self.simobj.location.y >self.lry:
			self.rx = randint(0,1)
			self.ry = randint(-1,1)
		elif self.simobj.location.y <= self.lry and self.simobj.location.x > self.lrx:
			self.rx = randint(-1,1)
			self.ry = randint(0,1)
		elif self.simobj.location.y <= self.lry and self.simobj.location.x <= self.lrx:
			self.rx = randint(0,1)
			self.ry = randint(0,1)
		else:
			self.rx = randint(-1,1)
			self.ry = randint(-1,1)
		if self.hrx == None or self.hry == None:
			return (self.rx*self.step,self.ry*self.step)
		if self.simobj.location.x >= self.hrx and self.simobj.location.y > self.lry:
			self.rx = randint(-1,0)
			self.ry = randint(-1,1)
		elif self.simobj.location.y >= self.hry and self.simobj.location.x >self.lrx:
			self.rx = randint(-1,1)
			self.ry = randint(-1,0)
		elif self.simobj.location.y >= self.hry and self.simobj.location.x >=self.hrx:
			self.rx = randint(-1,0)
			self.ry = randint(-1,0)

		return (self.rx*self.step,self.ry*self.step)

		
class Walk():
	def __init__(self,simobj):
		'''
		move Ai, makes an object move by the keyboard
		'''
		self.simobj = simobj
		self.step = 0
	def move(self,x=0,y=0):
		
		'''
		to make an object travel x and y distance from
		it original place.
		'''
		return x,y
		

class MoveToAPlace():
	def __init__(self,simobj,location=None):
		'''
		move to a place by mouse click
		'''
		self.simobj = simobj
		self.location = location
		self.step = 0.1
	def move(self,epsilon=0.001):
		'''
		move to an object, default step is 1,
		it is for monster move to play to attack the 
		player and also for other purpose of move to
		an object.
		'''
		if self.location == None:
			return 0,0
		if (self.simobj.location.x - self.location.x)**2 < epsilon and (self.simobj.location.y-self.location.y)**2<epsilon:
			return 0,0
		if self.simobj.location.x == self.location.x:
			if self.simobj.location.y < self.location.y:
				return 0,self.step
			else:
				return 0,-self.step
		elif self.simobj.location.y == self.location.y:
			if self.simobj.location.x < self.location.x:
				return self.step,0
			else:
				return -self.step,0
		else:
			if abs(self.simobj.location.x-self.location.x) > abs(self.simobj.location.y-self.location.y):
				if self.simobj.location.x < self.location.x:
					return self.step,self.getFormular(self.step,self.location,'y')
				else:
					return -self.step,self.getFormular(-self.step,self.location,'y')
			else:
				if self.simobj.location.y < self.location.y:
					return self.getFormular(self.step,self.location,'x'),self.step
				else:
					return self.getFormular(-self.step,self.location,'x'),-self.step

	def getFormular(self,step,other,getXOrY='x'):
		'''get walking direction
		args:
			step: what the moving distance each time
			other: other object that self to move to
			getXOrY: return x if y is known or y 
		'''
		scope = (self.simobj.location.y-other.y)/(self.simobj.location.x-other.x)
		b = self.simobj.location.y - self.simobj.location.x*scope 
		if getXOrY =='x':
			return ((self.simobj.location.y+step-b)/scope)-self.simobj.location.x
		else:
			return ((self.simobj.location.x+step)*scope+b)-self.simobj.location.y


class Chase():
	def __init__(self,simobj,enemy):
		'''
		chase an object move Ai
		'''
		self.simobj = simobj
		self.other = enemy.location
		self.step = 0.1
	def move(self,epsilon=1):
		'''
		move to an object, default step is 1,
		it is for monster move to play to attack the 
		player and also for other purpose of move to
		an object.
		'''
		if self.other == None:
			return 0,0
		if (self.simobj.location.x - self.other.x)**2 < epsilon and (self.simobj.location.y-self.other.y)**2<epsilon:
			return 0,0
		if self.simobj.location.x == self.other.x:
			if self.simobj.location.y < self.other.y:
				return 0,self.step
			else:
				return 0,-self.step
		elif self.simobj.location.y == self.other.y:
			if self.simobj.location.x < self.other.x:
				return self.step,0
			else:
				return -self.step,0
		else:
			if abs(self.simobj.location.x-self.other.x) > abs(self.simobj.location.y-self.other.y):
				if self.simobj.location.x < self.other.x:
					return self.step,self.getFormular(self.step,self.other,'y')
				else:
					return -self.step,self.getFormular(-self.step,self.other,'y')
			else:
				if self.simobj.location.y < self.other.y:
					return self.getFormular(self.step,self.other,'x'),self.step
				else:
					return self.getFormular(-self.step,self.other,'x'),-self.step
	def getFormular(self,step,other,getXOrY='x'):
		'''get walking direction
		args:
			step: what the moving distance each time
			other: other object that self to move to
			getXOrY: return x if y is known or y 
		'''
		scope = (self.simobj.location.y-other.y)/(self.simobj.location.x-other.x)
		b = self.simobj.location.y - self.simobj.location.x*scope 
		if getXOrY =='x':
			return ((self.simobj.location.y+step-b)/scope)-self.simobj.location.x
		else:
			return ((self.simobj.location.x+step)*scope+b)-self.simobj.location.y


class RunAway():
	def __init__(self,simobj,enemy):
		'''
		move away from an object move Ai
		'''
		self.simobj = simobj
		self.step = 0.1
		self.other = enemy.location
	def move(self,step=0.1):
		'''
		move away from an object, default step is 1,
		it is set for like animals walk away from it enemies
		or monsters walk away from player if the player is powerful
		'''
		if self.simobj.location.x > self.other.x and self.simobj.location.y > self.other.y:
			return step,step
		elif self.simobj.location.x > self.other.x and self.simobj.location.y < self.other.y:
			return step,-step
		elif self.simobj.location.x < self.other.x and self.simobj.location.y > self.other.y:
			return -step,step
		elif self.simobj.location.x < self.other.x and self.simobj.location.y < self.other.y:
			return -step,-step
		elif self.simobj.location.x == self.other.x and self.simobj.location.y > self.other.y:
			return step,step
		elif self.simobj.location.x == self.other.x and self.simobj.location.y < self.other.y:
			return step,-step
		elif self.simobj.location.x > self.other.x and self.simobj.location.y == self.other.y:
			return step,step
		elif self.simobj.location.x < self.other.x and self.simobj.location.y == self.other.y:
			return -step,step
		elif self.simobj.location.x == self.other.x and self.simobj.location.y == self.other.y:
			return step,step
		else:
			return 0,0



class Stand(Immovable):
	def __init__(self,x=0,y=0):
		super().__init__(x,y)
		
	def stand(self):
		pass
		
	def moveTo(self,x=0,y=0):
		print("You told me to don't move")
		
	def move(self,x=0,y=0):
		print("You told me to don't move")





if __name__ == '__main__':
	m = Movable(Location(0,1))
	b = Movable(Location(11,1))
	a = Walk(m)
	c = Walk(b)
	m.move(1,2)
	m.getPosition()