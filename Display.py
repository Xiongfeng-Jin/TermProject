"""
Author: Xiongfeng Jin

basic graph display for all the objects in the game. it also get
the user input and allow user control it character on the screen by
mouse or keyboard.
"""


import tkinter as tk
from gui_config import *
from Location import *
from MoveBehavior import *
from Visitor import PrintStateVisitor
printState = PrintStateVisitor()
center_x = WIDTH/2
center_y = HEIGHT/2
scale = SCALE
itemCounter = 0
root = tk.Tk()
canvas = tk.Canvas(root,width = WIDTH,height = HEIGHT)
canvas.pack()
root.update()
player = None

def simToScreen(x, y):
	"""Converts coordinates from simulation to screen coordinates"""
	x = x*SCALE
	y = -y*SCALE
	x += center_x
	y += center_y
	return (int(x),int(y))

def screenToSim(x, y):
	"""Converts screen coordinates to an approximate simulation coordinate"""
	y -= center_y
	x -= center_x
	y = -y/SCALE
	x = x/SCALE
	return (int(x),int(y))


def setControlPlayer(sim):
	"""
	set the user control object
	"""
	global player
	player = sim
	
def mhandle(event):
	"""
	define the interaction when user press the mouse
	"""
	global player
	if player == None:return
	for o in player._observers:
		if o._marker.bg =='blue':
			player.setMoveBehavior(Chase(player,o))
			return
	x,y = screenToSim(event.x,event.y)
	player.setMoveBehavior(MoveToAPlace(player,location=Location(x,y)))



canvas.bind("<Button>",mhandle)


def keyPressHandle(event):
	"""
	define the action when user press the key on the keyboard
	"""
	global player
	if player == None:return
	if event.keysym == "Up" or event.keysym == 'w':
		player.setMoveBehavior(Walk(player))
		player.move(0,0.1)
	elif event.keysym == 'Down' or event.keysym == 's':
		player.setMoveBehavior(Walk(player))
		player.move(0,-0.1)
	elif event.keysym == 'Left' or event.keysym == 'a':
		player.setMoveBehavior(Walk(player))
		player.move(-0.1,0)
	elif event.keysym == 'Right' or event.keysym == 'd':
		player.setMoveBehavior(Walk(player))
		player.move(0.1,0)
	elif event.keysym == '7':
		player.setMoveBehavior(RandomWalk(player,lrx=-20,lry=-20,hrx=20,hry=20))
	elif event.keysym == '1':
		print("start walk")
		player.setMoveBehavior(Walk(player))
	elif event.keysym == '2':
		for e in player._observers:
			if distance(player.location,e.location) < 2:
				player.attack(e) 
	elif event.keysym == '5':
		for e in player._observers:
			printState.visit(e)
	elif event.keysym == '3':
		player.display()
	elif event.keysym == '4':
		for e in player._observers:
			if distance(player.location,e.location) < 5:
				player.magicAttack('fireball',e) 
	elif event.keysym == '6':
		print("hp+1, now you have",player.hp,"hp")
		player.heal()
root.bind("<Key>",keyPressHandle)

def mouseOver(event):
	"""
	define the ation when user move mouse
	around on the screen
	"""
	if player == None:return
	x,y = screenToSim(event.x,event.y)
	temp = Location(x,y)
	for o in player._observers:
		if distance(o.location,temp)<1:
			o._marker.bg = 'blue'
		else:
			o._marker.bg = o._marker.fg
canvas.bind("<Motion>",mouseOver)



def createTag():
	"""
	create a unique tag for ever object on screen
	"""
	global itemCounter
	itemCounter += 1
	return "item" + str(itemCounter)


class NotDrawable(Exception):
	pass


class Drawable(object):
	def __init__(self):
		super().__init__()
		self.tag = createTag()
	def render(self,canvas):
		raise NotDrawable()

class Visual(object):
	def __init__(self,marker):
		self._marker = marker
	def getMarker(self):
		return self._marker


def display(drawable):
	"""
	put object on screen
	"""
	global canvas
	if isinstance(drawable,Visual):
		drawable = drawable.getMarker()

	canvas.delete(drawable.tag)
	drawable.render(canvas)

def undisplay(drawable):
	"""
	remove object from screen
	"""
	global canvas
	if isinstance(drawable,Visual):
		drawable = drawable.getMarker()

	canvas.delete(drawable.tag)

def refresh():
	root.update()

def forever():
	root.mainloop()

#################################################################################################
#Make markers

class BogusMarker(Exception):
	pass

class Marker(Drawable):
	"""
	base class for all the marker
	"""
	def __init__(self,simobj,*args):
		super().__init__(*args)
		self.simobj = simobj
	def render(self):
		raise BogusMarker()

	def circle(self,canvas,fill):
		loc = self.simobj.location
		ll=simToScreen((loc.x-0.5), (loc.y-0.5))
		ur=simToScreen((loc.x+0.5), (loc.y+0.5))
		canvas.create_oval(ll[0], ll[1], ur[0], ur[1], fill=fill, tags=self.tag)

class PlayerMarker(Marker):
	"""
	marke the player object
	"""
	def __init__(self,simobj):
		super().__init__(simobj)
		self.bg = 'green'
		self.fg = 'black'
	def setColor(self, color):
		self.bg = color
	def render(self,canvas):
		self.circle(canvas, self.bg)
		
		loc = self.simobj.location
		(x1, y1) = simToScreen(loc.x-0.5, loc.y-0.5)
		(x2, y2) = simToScreen(loc.x+0.5, loc.y-0.5)
		y2 = int(y2+5)
		canvas.create_rectangle(x1, y2, x2, y1, fill='white', tags=self.tag)
		color = 'red'
		if self.simobj.hp< 0:
			currentHp = 0
		else:
			currentHp = self.simobj.hp
		maxHp = self.simobj.maxHp
		hpPerecnt = currentHp/maxHp
		xd = (x2-x1)*hpPerecnt
		x2 = int(x1+xd)
		canvas.create_rectangle(x1, y2, x2, y1, fill=color, tags=self.tag)	

class MonsterMarker(Marker):
	"""
	marke the monster object
	"""
	def __init__(self,simobj):
		super().__init__(simobj)
		self.bg = 'red'
		self.fg = 'red'
	def setColor(self, color):
		self.bg = color
	def render(self,canvas):
		self.circle(canvas, self.bg)
		
		loc = self.simobj.location
		(x1, y1) = simToScreen(loc.x-0.5, loc.y-0.5)
		(x2, y2) = simToScreen(loc.x+0.5, loc.y-0.5)
		y2 = int(y2+5)
		canvas.create_rectangle(x1, y2, x2, y1, fill='white', tags=self.tag)

		currentHp = self.simobj.hp
		maxHp = self.simobj.maxHp
		hpPerecnt = currentHp/maxHp
		xd = (x2-x1)*hpPerecnt
		x2 = int(x1+xd)
		canvas.create_rectangle(x1, y2, x2, y1, fill=self.bg, tags=self.tag)
		
class NPCMarker(Marker):
	"""
	marke the npc object
	"""
	def __init__(self,simobj):
		super().__init__(simobj)
		self.bg = 'yellow'
		self.fg = 'black'
	def setColor(self, color):
		self.bg = color
	def render(self,canvas):
		self.circle(canvas, self.bg)
		
		loc = self.simobj.location
		(x1, y1) = simToScreen(loc.x-0.5, loc.y-0.5)
		(x2, y2) = simToScreen(loc.x+0.5, loc.y-0.5)
		y2 = int(y2+5)
		canvas.create_rectangle(x1, y2, x2, y1, fill='white', tags=self.tag)

		currentHp = self.simobj.hp
		maxHp = self.simobj.maxHp
		hpPerecnt = currentHp/maxHp
		xd = (x2-x1)*hpPerecnt
		x2 = int(x1+xd)
		canvas.create_rectangle(x1, y2, x2, y1, fill=self.bg, tags=self.tag)
		
class AttackMarker(Marker):
	"""
	marke the attack object
	"""
	def __init__(self,simobj):
		super().__init__(simobj)
		self.x = 0
		self.y = 0
	def render(self,canvas):
		txt = "-"+str(self.simobj.damage)
		x,y = simToScreen(self.x,self.y+1)
		canvas.create_text(x,y, anchor=tk.CENTER, justify=tk.CENTER, tags=self.tag, text=txt)
		
class MagicMarker(Marker):
	"""
	base class for marke the magic object
	"""
	def __init__(self,simobj):
		super().__init__(simobj)
		pass
	def render(self,canvas):
		pass


class FireballMarker(Marker):
	"""
	marke the fireball object
	"""
	def __init__(self,simobj):
		super().__init__(simobj)
		self.x = 0
		self.y = 0
	def render(self,canvas):
		txt = "-"+str(self.simobj.damage)
		txt1 = "Fireball!"
		x,y = simToScreen(self.x,self.y+1)
		x1,y1 = simToScreen(self.simobj.simobj.location.x,self.simobj.simobj.location.y+1)
		canvas.create_text(x,y, anchor=tk.CENTER, justify=tk.CENTER, tags=self.tag, text=txt)
		canvas.create_text(x1,y1, anchor=tk.CENTER, justify=tk.CENTER, tags=self.tag, text=txt1)


class ImageMarker(Marker):
	"""
	marke the image object
	"""
	def __init__(self,simobj):
		super().__init__(simobj)

	def render(self,canvas):
		(x,y) = simToScreen(self.simObj.location.x, self.simObj.location.y)
		canvas.create_image(x, y, image=images[NPC_image], anchor=tk.CENTER, tags=self.tag)


if __name__ == '__main__':
	pass