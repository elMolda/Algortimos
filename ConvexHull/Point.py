class Point:
	def __init__(self,x,y):
		self.x = double(x)
		self.y = double(y)
	def __str__(self):
		return "(%s, %s)" % (self.x, self.y)
