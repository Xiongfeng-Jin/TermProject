"""
Author: Xiongfeng Jin

This class is for the Observer pattern
"""

class Observer(object):
	'''Observers some other object in the simulation'''

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def recieveNotification(self, other):
		'''Executes when a notification from other is recieved'''
		pass

class Observable(object):
	'''Can be observed by observers'''

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._observers = []

	def addObserver(self, other):
		'''Adds an observer'''
		self._observers.append(other)

	def removeObserver(self, other):
		'''Removes an observer, if it is already observing this object'''
		if other in self._observers:
			self._observers.remove(other)

	def notifyObservers(self):
		'''Sends a notification to all of the observers observing this object'''
		for o in self._observers:
			o.recieveNotification(self)