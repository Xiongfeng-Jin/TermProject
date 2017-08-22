"""
Author: Xiongfeng Jin

This file defines all the state that monster have. each state
defines different action that monster do
"""
from MoveAI import *
class State():
	"""
	base class for all state
	"""
	def __init__(self,simobj):
		self.simobj = simobj
		self.printSwitch = True
	def attack(self):
		pass



class Angry(State):
	"""
	angry state, when monster get angry, it chase the
	player and attack them
	"""
	def __init__(self,simobj):
		super().__init__(simobj)
	def MoveAI(self,enemy):
		self.simobj.moveBehavior = Chase(self.simobj,enemy)
	def madWith(self,enemy):
		self.MoveAI(enemy)
	def attack(self,enemy):
		self.simobj.attack(enemy)
	def __str__(self):
		return self.simobj.name + " is angry"


class Uncare(State):
	"""
	Uncare state, when the monster in the Uncare state, 
	it does not attack anyone, and it move Randomly
	"""
	def __init__(self,simobj):
		super().__init__(simobj)
	def MoveAI(self):
		self.simobj.moveBehavior = RandomWalk(self.simobj,lrx=-20,lry=-20,hrx=20,hry=20)
	def attack(self,enemy):
		print(self.simobj.name,"does not care about you")
	def __str__(self):
		return self.simobj.name + " is uncare"

class Scare(State):
	"""
	scare state, when monster scared it RunAway from the player
	"""
	def __init__(self,simobj):
		super().__init__(simobj)
	def MoveAI(self):
		self.simobj.moveBehavior = RunAway(self.simobj,enemy)
	def scareFrom(self,enemy):
		self.MoveAI(enemy)
	def attack(self,enemy):
		print(self.simobj.name,"is afriad to attack you")
	def __str__(self):
		return self.simobj.name + " is scared"

class Annoyed(State):
	"""
	annoyed state, when monster get annoyed it may be get
	angry and attack the player
	"""
	def __init__(self,simobj):
		super().__init__(simobj)
		self.annoying = 0
	def MoveAI(self):
		self.simobj.moveBehavior = RandomWalk(self.simobj,lrx=-20,lry=-20,hrx=20,hry=20)
	def __add__(self,other):
		self.annoying += other
		return self.annoying
	def madWith(self,enemy):
		if self.annoying == 300:
			self.simobj.state = self.simobj.angry
			self.simobj.state.madWith(enemy)
		else:
			self.annoying += 1
	def attack(self,enemy):
		if self.printSwitch:
			print("if you do not go away from",self.simobj.name,"it will attack you")
			self.printSwitch = False
	def __str__(self):
		return self.simobj.name + " is Annoyed"