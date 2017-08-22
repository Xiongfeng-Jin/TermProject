"""
Author: Xiongfeng Jin

This file defines all the visitors, contain rain-visitor and print-state-visitor
"""
class Visitor(object):
	"""
	super class for all the visitor
	"""
	def visit(self,other):
		pass
		
		
class RainVisitor(Visitor):
	"""
	rain visitor, makes the groud wet so objects will slip when they move
	"""
	def __init__(self,rainLevel):
		if rainLevel < 10:
			self.slip = 0.1
		elif rainLevel < 11:
			self.slip = 0.2
		elif rainLevel < 12:
			self.slip = 0.4
		else:
			self.slip = 0.6
	def visit(self,other):
		other.moveBehavior.step = self.slip


class PrintStateVisitor(Visitor):
	"""
	print the state of the monster
	"""
	def visit(self,other):
		print(other.state)