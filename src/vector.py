import math as math 
from allowed_types import ALLOWED_TYPES

class Vector:
	"""" Vector Class """  
	def __init__(self, x, y):
		""" new object """ 
		if type(x) not in ALLOWED_TYPES:
			raise TypeError("Argument not compatible")
		if type(y) not in ALLOWED_TYPES:
			raise TypeError("Argument not compatible")
		self._x = x 
		self._y = y 

	def __str__(self):
		""""triggers when used print function """
		return f"{self._x}:{self._y}"

	def __repr__(self):
		""""representation of the vector object """
		return f"({self._x}, {self._y})"

	def getX(self):
		""""returns x value of vector object """
		return self._x

	def getY(self):
		""""returns y value of vector object """
		return self._y 

	def setX(self, newvalue):
		""""sets x value to newvalue """
		if newvalue != int and newvalue != float:
			raise TypeError("New value not a compatible datatype")
		self._x = newvalue

	def setY(self, newvalue):
		""""sets y value to newvalue  """
		if newvalue != int and newvalue != float:
			raise TypeError("New value not a compatible datatype")
		self._y = newvalue

	def __add__(self, other):
		""""function triggers when used + """
		if not isinstance(other, Vector):
			raise TypeError("Instance not of class Vector")
		return self._x + other._x, self._y + other._y

	def __sub__(self, other):
		""""function triggers when used - """
		if not isinstance(other, Vector):
			raise TypeError("Instance not of class Vector")
		return self._x - other._x, self._y - other._y

	def __mul__(self, scalar):
		""""function triggers when used * """
		if type(scalar) not in ALLOWED_TYPES:
			raise TypeError("Scalar value of wrong datatype")
		return self._x * scalar, self._y * scalar

	def distance(self, other):
		""""returns the distance of the points"""
		if not isinstance(other, Vector):
			raise TypeError("Instance not of Vector Class")
		distance_var = ( (other.getX() - self.getX()) ** 2 ) + ( (other.getY() - self.getY()) ** 2 )  
		result = round(math.sqrt(distance_var), 2)
		return  str(result) + " units"

