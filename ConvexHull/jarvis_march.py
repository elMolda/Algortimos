import sys
from Point import Point
import matplotlib.pyplot as plt
from sampler import rectangular_sample, eliptical_sample

def distance(a,b,c):
	y1 = a.y - b.y
	y2 = a.y -c.y
	x1 = a.x -b.x
	x2 = a.x -c.x
	x = y1 * y1 + x1 * x1
	y = y2 * y2 + x2 * x2

	if x == y:
		return 0
	elif x < y:
		return -1
	else:
		return 1

def crossProdcut(a,b,c):
	y1 = a.y - b.y
	y2 = a.y - c.y
	x1 = a.x - b.x
	x2 = a.x - c.x
	return y2 * x1 - y1 * x2

def jarvis_hull(points):
	start = points[0]
	for i in range(1,len(points)):
		if points[i].x < start.x:
			start = points[i]

	current = start
	result = set()
	result.add(start)
	colinear = []
	while True:
		nextTarget = points[0]
		for i in range (1,len(points)):
			if points[i] == current:
				continue

			val = crossProdcut(current,nextTarget,points[i])
			if val > 0:
				nextTarget = points[i]
				colinear = []
			elif val == 0:
				if distance(current,nextTarget,points[i]) < 0:
					colinear.append(nextTarget)
					nextTarget = points[i]
				else:
					colinear.append(points[i])

		for i in range(0,len(colinear)):
			result.add(colinear[i])

		if nextTarget == start:
			break

		result.add(nextTarget)
		current = nextTarget

	return result

n = int(sys.argv[1])
fig = str(sys.argv[2])
a = int(sys.argv[3])
b = int(sys.argv[4])
r = float(sys.argv[5])
'''sample = []
	a1 = Point(0, 0)
	a2 = Point(0, 4)
	a3 = Point(-4, 0)
	a4 = Point(5, 0)
	a5 = Point(0, -6)
	a6 = Point(1, 0)
	sample.append(a1)
	sample.append(a2)
	sample.append(a3)
	sample.append(a4)
	sample.append(a5)
	sample.append(a6)'''



if fig == 'r':
	sample  = rectangular_sample(n,a,b,r)
		
elif fig == 'e':
	sample  = eliptical_sample(n,a,b,r)

hull = jarvis_hull(sample)
		
x_hull = []
y_hull = []

for p in hull:
	print(str(p))
	x_hull.append(p.x)
	y_hull.append(p.y)

x = []
y = []
for i in range(len(sample)):
	x.append(sample[i].x)
	y.append(sample[i].y)

plt.scatter(x,y)
plt.scatter(x_hull,y_hull,facecolor='red')
plt.show()