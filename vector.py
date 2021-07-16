import math 

class Vector(object):
	""" Vector Class """
	def __init__(self, x, y):
		""" constructor """
		self._x = x
		self._y = y
		 	
	def getX(self):
		""" returns x value """
		return self._x
		
	def getY(self):
		""" returns y value """
		return self._y
		
	def setX(self, newvalue):
		""" sets x value to new value """
		self._x = newvalue
		
	def setY(self, newvalue):
		""" sets y value to new value """
		self._y = newvalue
		
	def magnitude(self, other):
		""" returns magnitude of the vector """
		magnitude_var = math.sqrt((other.getX() - self.getX()) ** 2  + (other.getY() - self.getY()) ** 2)
		return round(magnitude_var)
			 			 	
	def __str__(self):
		""" calls when used print function """
		return str(self._x) + ", " + str(self._y)
		
	def __repr__(self):
		""" representation """
		return '({}, {})'.format(str(self._x), str(self._y))
		
	def __add__(self, other):
		""" adds two vector and returns """
		return self.getX() + other.getX(), self.getY() + other.getY()
		
	def __sub__(self, other):
		""" returns the difference of two vectors """
		return self.getX() - other.getX(), self.getY() - other.getY()
		
	def __mul__(self, other):
		""" returns the product of the vector multiplied by a scalar """
		return self.getX() * other, self.getY() * other
											
