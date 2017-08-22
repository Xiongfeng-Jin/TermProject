"""
Author: Xiongfeng Jin

Monster decorater that decorate monster to a monster boss or
any other type of monster if needed
"""
from Monster import Monster

class MonsterDecorator(Monster):
	"""
	base class for monster decorater
	"""
	def __init__(self,decorated):
		self.decorated = decorated
		self._marker = self.decorated._marker


class MonsterBoss(MonsterDecorator):
	"""
	decorate a monster to be a boss
	"""
	def __init__(self,decorated):
		super().__init__(decorated)
	def becomeBoss(self):
		self._marker.bg = self._marker.fg = "black"
		self.decorated.exp=100
		return self.decorated


if __name__ == '__main__':
	a = Monster('A')
	a = MonsterBoss(a).becomeBoss()
	a.display()
	a.getPosition()
	while a.location.x<2.1:
		a.move()
		a.getPosition()