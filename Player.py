"""
Author: Xiongfeng Jin

THis is the class for players, it set all the behaviors that
a plyaer can do.
"""
from AliveObject import *
from AttackAI import Attack,Magic,FireBall
import time
class Player(AliveObject,Movable,Observable):
	def __init__(self,name,lv=1,location=Location(0,0)):
		'''
		all player start lv 1, and set it maxhp and maxmp is 10 time it lv
		and the attack damage is equal to it lv, the basic move behavior is walk
		'''
		AliveObject.__init__(self,name,lv)
		Movable.__init__(self,location)
		Visual.__init__(self,PlayerMarker(self))
		Observable.__init__(self)
		self.moveBehavior = Walk(self)
		self.personality = PlayerPersonality()
		self.picture = 'npc.gif'
		self.maxHp = lv * 10
		self.maxMp = lv*10
		self.attackAI = Attack(self)
		self.magic = Magic(self)
		self.attackPeriod = 30
		self.attackDelay = 30
		self.magicList = {'fireball':FireBall(self)}
		
	def attack(self,other):
		'''
		it attack the monster and when the monster died, user gets the
		exp from the monster, when the exp reached to 100 or above, player
		will level up, and call the lvUp method to set the damage and hp and
		mp so on.
		'''
		if self.attackPeriod == self.attackDelay:
			self.attackAI.attack(other)
			self.attackPeriod = 0
		self.attackPeriod += 1

			

	def setMagic(self,mg):
		'''
		set the magic user want to use
		'''
		self.magic = mg
		
	def magicAttack(self,mg,other):
		'''
		use magic attack the monster
		'''
		mg = self.magicList[mg]
		if self.attackPeriod == self.attackDelay:
			self.setMagic(mg)
			self.magic.attack(other)
			self.attackPeriod = 0
		self.attackPeriod += 1

		
	def heal(self):
		'''
		heal self, hp + 1
		'''
		self.hp += 1
		self.mp -= 1
		if self.hp >= self.maxHp:
			self.hp = self.maxHp
			
	def lvUp(self,lv):
		'''
		when level up, all hp and mp will be full and maxhp, maxmp
		and damage will increase 
		'''
		self.maxHp = lv *10
		self.maxMp = lv *10
		self.hp = self.maxHp
		self.mp = self.maxMp
		self.attackAI.damage = lv
		
	def display(self):
		'''
		display the player"s status
		'''
		super().display()
		print("Attack damege:",self.attackAI.damage)
		
	def setLv(self,lv):
		'''
		to set the players lv, debuging only.
		this method may never be called by the user.
		'''
		self.lv = lv
		self.lvUp(self.lv)

	def move(self,x=0,y=0):
		if isinstance(self.moveBehavior,Walk):
			super().move(x,y)
			self.notifyObservers()
			return
		x,y = self.moveBehavior.move()
		super().move(x,y)
		self.notifyObservers()

		

if __name__ == '__main__':
	a = Player('A')
	a.say()
	b = Player('B',location=Location(10,10))
	print(isinstance(a,Player))
	b.exp = 1000
	a.getPosition()
	for x in range(10):
		a.attack(b)
	a.display()
	print(type(a.location))
	setControlPlayer(a)
	refresh()
	a.setMoveBehavior(RandomWalk(a))
	while True:
		display(a)
		a.move()
		time.sleep(.01)
		refresh()
	forever()