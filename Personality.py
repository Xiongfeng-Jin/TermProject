"""
Author: Xiongfeng Jin

this class is for all the object that are alive. it defines different Personality
for each object.
"""

class Personality:
	def say(self):
		print("I am an alive oject")


class PlayerPersonality():
	def __init__(self):
		self.kind = "Player"
		self.peace = "Normal"
		self.kill = "Normal"
		self.love = "Normal"
	def say(self):
		print("I am a",self.kind)

class NpcPersonality():
	def __init__(self):
		self.kind = "NPC"
		self.peace = "High"
		self.kill = "None"
		self.love = "High"
	def say(self):
		print("I am a",self.kind)


class MonsterPersonality():
	def __init__(self):
		self.kind = "Monster"
		self.peace = "low"
		self.kill = "High"
		self.love = "low"
	def say(self):
		print("I am a",self.kind)