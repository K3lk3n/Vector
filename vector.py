import math 

class Vector(object):
	""" Vector Class """
	def __init__(self, x, y):
		""" constructor """
		self._x = x
		self._y = y
		 	
	def getX(self):
		""" returns x value of vector object"""
		return self._x
		
	def getY(self):
		""" returns y value of vector object  """
		return self._y
		
	def setX(self, newvalue):
		""" set new value to x  """
		self._x = newvalue
		
	def setY(self, newvalue):
		""" sets new value to y  """
		self._y = newvalue
		
	def magnitude(self, other):
		""" returns magnitude of the vector object """
		magnitude_var = math.sqrt((other.getX() - self.getX()) ** 2  + (other.getY() - self.getY()) ** 2)
		return round(magnitude_var)
			 			 	
	def __str__(self):
		""" returns string version of the vector object """
		return str(self._x) + ", " + str(self._y)
		
	def __repr__(self):
		""" representation of the vector object  """
		return '({}, {})'.format(str(self._x), str(self._y))
		
	def __add__(self, other):
		""" returns the sum of two vectors """
		return self.getX() + other.getX(), self.getY() + other.getY()
		
	def __sub__(self, other):
		""" returns the difference of two vectors """
		return self.getX() - other.getX(), self.getY() - other.getY()
		
	def __mul__(self, other):
		""" returns the product of the vector and a scalar """
		return self.getX() * other, self.getY() * other
											
