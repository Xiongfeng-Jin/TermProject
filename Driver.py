"""
Author: Xiongfeng Jin

simulation file, basic game structure.
"""
from Player import *
from Monster import *
from MonsterDecorator import MonsterBoss
from NPC import *
from Visitor import RainVisitor
import time
from random import random, randint

objlist = []
name = "Player"
me = Player(name)
objlist.append(me)

mlist = [['Goblin', 1], ['Osiris', 2], ['Baphomet', 3], ['Doppelganger', 4], ['Mistress', 5], ["Golden'Thief'Bug", 6], ["Orc'Hero", 7], ['Drake', 8], ['Eddga', 9], ['Maya', 10], ["Moonlight'Flower", 11], ['Pharaoh', 12], ['Phreeoni', 13], ["Orc'Lord", 14], ["Stormy'Knight", 15], ['Garm', 16], ["Dark'Lord", 17], ["Turtle'General", 18], ["Lord'of'Death", 19], ['Dracula', 20], ["Evil'Snake'Lord", 21], ["Incantation'Samurai", 22], ["Pori'Pori", 23], ["Amon'Ra", 24], ["Tao'Gunka", 25], ["RSX'0806", 26], ['Bacsojin', 27], ["Lord'Knight'Seyren", 28], ["Assassin'Cross'Eremes", 29], ["Whitesmith'Harword", 30], ["High'Priest'Magaleta", 31], ["Sniper'Shecil", 32], ["High'Wizard'Katrinn", 33], ['Ygnizem', 34], ['Vesper', 35], ["Lady'Tanee", 36], ['Thanatos', 37], ['Detale', 38], ["Kiel'D-01", 39], ["Valkyrie'Randgris", 40], ["Gloom'Under'Night", 41], ['Ktullanux', 42], ['Atroce', 43], ['Ifrit', 44], ["Fallen'Bishop", 45], ['Beelzebub', 46], ['Gopinich', 47], ['Morroc', 48]]
def getMonster(lv):
	"""
	generate a monster randomly based on the player's level
	"""
	locx = randint(-20,20)
	locy = randint(-20,20)
	if lv > 47:
		lv = 47
	m = randint(0,lv)
	it = Monster(mlist[m][0],lv=mlist[m][1],enemy = [me],location=Location(locx,locy))
	if it.lv == 1 or it.lv ==48:
		it = MonsterBoss(it)
		return it.becomeBoss()
	return it


rain = RainVisitor(0)
def isRaining():
	global rain
	r = randint(0,100)
	rl = randint(0,13)
	rain = RainVisitor(rl)
	if r <= 20:
		return True
	else:
		return False
	


def main():
	count = 0
	#print instruction
	print("instruction: Hoding '2' to kill the monster\npress 3 to show the self status\npress 4 to use magic\npress 5 to show the monster's state\npress 6 to heal your self\nyou can use 'w,a,s,d' keys to move or you can mouse over the monster, the monster will become blue color, then you click")
	setControlPlayer(me)
	refresh()
	npc = NPC('npc',me._observers)
	for x in objlist:
		display(x)
	while True:
		count += 1
		if len(me._observers) < me.lv:
			if npc in objlist:
				objlist.remove(npc)
				undisplay(npc)
			it = getMonster(me.lv)
			npc = NPC('npc',me._observers)
			objlist.append(npc)
			objlist.append(it)
		refresh()
		time.sleep(.01)
		for x in objlist:
			if x.alive == False and not isinstance(x,Player):
				objlist.remove(x)
			if isRaining():
				rain.visit(x)
			x.move()
			if count == 50:
				for x in objlist:
					if not isinstance(x,NPC):
						undisplay(x.attackAI)
						undisplay(x.magic)
				count = 0
			if x.alive == True or isinstance(x,Player):
				display(x)
	forever()
	
	
if __name__ == "__main__":
	main()