"""
Author: Xiongfeng Jin

this is the model of the Attack behavior, creates Attack behavior instance in the
Player and Monster class control attack type
"""
from Display import Visual,AttackMarker,MagicMarker,FireballMarker,display,undisplay
class Attack(Visual):
	"""
	Basic attack AI, take the enemy and subtrack it hp.
	"""
	def __init__(self,simobj):
		self.damage = simobj.lv
		self.simobj = simobj
		Visual.__init__(self,AttackMarker(self))
	def attack(self,other):
		"""
		attack the enemy and attack, if the enemy died, and the attacker is
		the player, then player get the exp from the Monster
		"""
		self._marker.x = other.location.x
		self._marker.y = other.location.y
		if other.hp <= 0:return
		undisplay(self)
		other.hp -= self.damage
		display(self)
		if other.hp <= 0:
			other.die()
			if self.simobj.personality.kind == "Player":
				self.simobj.exp += other.exp
				if self.simobj.exp >= 100:
					self.simobj.lv += self.simobj.exp // 100
					self.simobj.exp = self.simobj.exp % 100
					self.simobj.lvUp(self.simobj.lv)
					print("Congratulation! Now you are level",self.simobj.lv)




class Magic(Visual):
	"""
	the interface for all the magic, it the base class for the
	magic attack
	"""
	def __init__(self,simobj):
		self.damage = 0
		self.exp = 0
		self.lv = 1
		self.simobj = simobj
		Visual.__init__(self,MagicMarker(self))
	def attack(self):
		print("you don't know any magic yet")

class FireBall(Magic):
	"""
	baisc fire magic, attack the enmey by using fire
	"""
	def __init__(self,simobj):
		super().__init__(simobj)
		self.damage = 5*self.lv
		self.needMp = 4+self.lv
		Visual.__init__(self,FireballMarker(self))
	def attack(self,other):
		"""
		take the enemy attack by fire magic, when the enmey died, and if the
		attacker is player, then player get the exp from the monster
		"""
		self._marker.x = other.location.x
		self._marker.y = other.location.y
		if self.simobj.mp < self.needMp:
			print("mp not enough")
			return
		if other.hp <= 0:
			return
		else:
			undisplay(self)
			other.hp -= self.damage
			self.simobj.mp -= self.needMp
			print('Fire Ball!')
			display(self)
			if other.hp <= 0:
				other.die()
				if self.simobj.personality.kind == "Player":
					self.simobj.exp += other.exp
					if self.simobj.exp >= 100:
						self.simobj.lv += self.simobj.exp // 100
						self.simobj.exp = self.simobj.exp % 100
						self.simobj.lvUp(self.simobj.lv)
						print("Congratulation! Now you are level",self.simobj.lv)