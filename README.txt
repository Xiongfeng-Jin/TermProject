Run Driver.py

Dependencies:
	this program is running on the python 3.3 or above. use either pycharm or terminal to run this program.


Pattern Use:
	 Strategy Pattern:
	 	the file personality is the description of each characters, and when the "say()" method are called in the superclass, which is the AliveObject class, each character say something different.
	 	files that are strategy pattern related are: Personality.py
	 	pattern used in Player.py, NPC.py, Monster.py, AliveObject.py

	 Observer Pattern:
	 	the observer file is the file which implement the observer pattern. in the program, monsters are observing player's movement in order to react. NPC is observing the monsters to aovid the monsters.
	 	files related to observer pattern: Observer.py
	 	pattern used in NPC.py, Player.py, Monster.py

	 Decorator Pattern:
	 	in the program decorator pattern is decorating the monster to make it become a boss. the decorator class changes monster's color and its exp.
	 	files related to decorator pattern: MonsterDecorator
	 	patern used in Driver.py

	 State Pattern:
	 	state pattern includes Angry, Uncare, Scare, Annoyed, four states. monsters will switch between these states. each state has the attack method, when the monsters are in the different state, the attack method will not be the same.
	 	files related to state pattern: State.py
	 	pattern used in Monster.py

	 Visitor Pattern:
	 	the RainVisitor visit both players and monsters and makes them to slip depend on how big the rain is. the printState visitor only visit the monsters and print what is the monster's current state.
	 	files related to visitor pattern: Visitor.py
	 	pattern used in Driver.py and Display.py(in the keypress event handler)


	General Thoughts:
		the driver file is Driver.py
		this program is a simple program, which does not do so many things. it just a simple game, where player is the green cycle and monsters are either red cycle and the black cycle. user can mouse over the monster and click to kill the monster or user "wsad" to move themsalves.
