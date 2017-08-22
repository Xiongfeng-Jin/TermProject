"""
Author: Xiongfeng Jin

this is the super class for all the monsters in the game,
it set the basic behavior that a monster has.
"""
from AliveObject import *
from AttackAI import Attack,Magic
from State import *
class Monster(AliveObject,Movable,Observer,Observable):
	def __init__(self,name,lv=1,enemy=[],location=Location(2,2)):
		'''
		all monster start lv 1, and set it maxhp and maxmp is 10 time it lv
		and the attack damage is equal to it lv, and exp is 9 plus it lv and
		the basic move behavior is walk
		'''
		AliveObject.__init__(self,name,lv)
		Movable.__init__(self,location)
		Visual.__init__(self,MonsterMarker(self))
		Observer.__init__(self)
		Observable.__init__(self)
		self.moveBehavior = RandomWalk(self,lrx=-20,lry=-20,hrx=20,hry=20)
		self.maxHp = lv * 10
		self.maxMp = lv * 10
		self.personality = MonsterPersonality()
		self.attackAI = Attack(self)
		self.exp =  9+lv
		self.magic = Magic(self)
		self.ml = []
		self.enemy = enemy
		self.state = State(self)
		self.angry = Angry(self)
		self.annoyed = Annoyed(self)
		self.uncare = Uncare(self)
		self.scare = Scare(self)
		self.printSwitch = True
		if len(enemy) >0:
			for e in enemy:
				e.addObserver(self)
		self.attackPeriod = 0
		self.attackDelay = 100
		
	def attack(self,other):
		'''
		attack the player, when player"s hp is less than 0
		then stop attacking. 
		'''
		if self.attackPeriod == self.attackDelay:
			self.attackAI.attack(other)
			self.attackPeriod = 0
		self.attackPeriod += 1
	
	def setMagic(self,mg):
		'''
		set the magic monster want to use
		'''
		self.magic = mg
		
	def magicAttack(self,mg,other):
		'''
		use magic attack the player
		'''
		mg = self.magicList[mg]
		if self.attackPeriod == self.attackDelay:
			self.setMagic(mg)
			self.magic.attack(other)
			self.attackPeriod = 0
		self.attackPeriod += 1
		
	def display(self):
		'''
		display the status of the monster.
		'''
		super().display()
		print("Attack damege:",self.attackAI.damage)
		
		
	def die(self):
		super().die()
		if len(self.enemy) >0:
			for e in self.enemy:
				e.removeObserver(self)
		undisplay(self)
		undisplay(self.attackAI)
		
	def move(self):
		x,y = self.moveBehavior.move()
		super().move(x,y)
		self.notifyObservers()
		
	def recieveNotification(self,o):
		if distance(self.location,o.location)<2:
			if self.hp < self.maxHp and self.printSwitch:
				print("you attacked",self.name,"it become angry")
				self.state = self.angry
				self.state.madWith(o)
				self.printSwitch = False
			self.state.attack(o)
			self.state.madWith(o)
		elif distance(self.location,o.location) <= 10:
			if self.state == self.angry:
				self.state.madWith(o)
				return
			self.state = self.annoyed
			self.state.madWith(o)
		elif distance(self.location,o.location) > 10:
			if self.state == self.angry:
				self.state.madWith(o)
				return
			self.state = self.uncare
			self.annoyed.annoying = 0
			self.setMoveBehavior(RandomWalk(self,lrx=-20,lry=-20,hrx=20,hry=20))
			

		
		
		
		
		

if __name__ == '__main__':
	a = Monster('A')
	b = Monster('B')
	a.location = Location(10,10)
	b.location = Location(-10,-10)
	display(a)
	display(a.attackAI)
	display(b)
	forever()
	a.magicAttack(Magic,b)