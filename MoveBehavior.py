"""
Author: Xiongfeng Jin

this is the interface for all the move behavior, it gethers all the
move behavior, so it eaiser to know how many move behaviors there are.
"""
from MoveAI import *


class MoveBehavior(Movable):
	def __init__(self,x=0,y=0):
		super().__init__(x,y)
