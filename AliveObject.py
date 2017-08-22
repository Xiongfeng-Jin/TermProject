"""
Author: Xiongfeng Jin

THis is the super class for all the alive object in the game, include
NPCs, Animals, monsters and players.
"""
from MoveBehavior import *
from Display import *
from Observer import *
from Personality import *
class AliveObject(Visual):
	def __init__(self,name,lv=1):
		'''
		all alive objects have hp, mp, lv, exp and move behaviors.
		'''
		self.name = name
		self.hp = lv* 10
		self.mp = lv *10
		self.lv = lv
		self.exp = 0
		self.moveBehavior = MoveBehavior()
		self.personality = Personality()
		self.alive = True


		
	def setMoveBehavior(self,mb):
		'''
		to change move behavior
		'''
		self.moveBehavior = mb
		
		
	def display(self):
		'''
		to show the status on the screen
		'''
		#self.pic.display()
		print("name:",self.name)
		print("hp:",self.hp)
		print("mp:",self.mp)
		print("level:",self.lv)
		print("exp:",self.exp)

	def say(self):
		self.personality.say()
		
	def die(self):
		'''
		it state self is died
		'''
		print(self.name,"died")
		self.alive = False
		#self.delete()