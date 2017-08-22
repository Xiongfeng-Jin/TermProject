"""
Author: Xiongfeng Jin

it the super class for all the NPCs, and it set the basic
behavoirs for all the npcs.
"""

from AliveObject import *
class NPC(AliveObject,Movable,Observable,Observer):
	def __init__(self,name,enemy=[],location=Location(-2,-2)):
		AliveObject.__init__(self,name)
		Movable.__init__(self,location)
		Visual.__init__(self,NPCMarker(self))
		Observable.__init__(self)
		Observer.__init__(self)
		self.moveBehavior = Walk(self)
		self.personality = NpcPersonality()
		self.picture = 'npc.gif'
		self.maxHp = self.lv *10
		self.enemy = enemy
		if len(enemy) > 0:
			for e in enemy:
				e.addObserver(self)
	def move(self):
		x,y = self.moveBehavior.move()
		super().move(x,y)
		self.notifyObservers()
		
	def display(self,x,y,pi):
		super().display()		
		
	def die(self):
		super().die()
		if len(self.enemy) >0:
			for e in self.enemy:
				e.removeObserver(self)
		undisplay(self)
		
	def notifyObservers(self):
		'''Sends a notification to all of the observers observing this object'''
		for o in self._observers:
			o.recieveNotification(self)
			
	def recieveNotification(self,o):
		if distance(self.location,o.location) <= 6:
			self.setMoveBehavior(RunAway(self,o))
			self.move()
		elif distance(self.location,o.location) > 6:
			self.setMoveBehavior(RandomWalk(self,lrx=-20,lry=-20,hrx=20,hry=20))



if __name__ == '__main__':
	gm = NPC("GM")
	display(gm)
	gm.setMoveBehavior(RandomWalk(gm,lrx=-20,lry=-20))
	while True:
		refresh()
		gm.move()
		display(gm)
	forever()