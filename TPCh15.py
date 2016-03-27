import math


class Point:
	"""represents a point in 2D space"""


blank = Point()
print(blank)
		
blank.x = 3.0
blank.y = 4.0
print((blank.x, blank.y)) #=> (3.0, 4.0) 


def print_point(object):
	print('(%g, %g)' % (object.x, object.y) )

print_point(blank) #=> (3, 4)


def distance_between_points(obj1, obj2):
	return math.sqrt((obj1.x - obj2.x)**2 + (obj1.y - obj2.y)**2)

point1 = Point()
point1.x = 6
point1.y = 2
print(distance_between_points(blank, point1)) #=> 3.605551275463989


class Rectangle:
	"""represents a rectangle

	attributes: width, height, corner"""


box = Rectangle()
box.width = 100
box.height = 200
box.corner = Point()
box.corner.x = 0
box.corner.y = 0


def get_center(obj):
	p = Point()
	p.x = obj.corner.x + obj.width/2
	p.y = obj.corner.y + obj.height/2
	return p

center = get_center(box)
print_point(center) #=> (50, 100)
print((box.width, box.height)) #=> (100, 200)


#objects are mutable

def grow_rectangle(rectangle, xgrow, ygrow):
	rectangle.width += xgrow
	rectangle.height += ygrow

grow_rectangle(box, 50, 50)

newcenter = get_center(box)
print_point(newcenter) #=> (75, 125)
print((box.width, box.height)) #=> (150, 250)


def move_rectangle(rect, xmove, ymove):
	rect.corner.x += xmove
	rect.corner.y += ymove

print('--move rec--')
print_point(box.corner) #=> (0, 0)
move_rectangle(box, 20, 10)
print_point(box.corner) #=> (20, 10)


#copying is an alternative to aliasing

p1 = Point()
p1.x = 3.0
p1.y = 4.0

p2 = p1

print_point(p1) #=> (3, 4)
print_point(p2) #=> (3, 4)

p1.x = 8

print_point(p1) #=> (8, 4)
print_point(p2) #=> (8, 4)
print(p1 is p2) #=> True
print(p1 == p2) #=> True

import copy

p2 = copy.copy(p1)
print(p1 is p2) #=> False
print(p1 == p2) #=> False

"""
'==' is not equivalence for instances. It is the same as the 'is' operator- it
checks identity.
"""

print("--box2--")
box2 = copy.copy(box)
print(box2 is box) #=> False
print(box2.corner is box.corner) #=> True

print(box.corner.x) #=> 20
print(box2.corner.x) #=> 20

box.corner.x = 10.5

print(box.corner.x) #=> 10.5
print(box2.corner.x) #=> 10.5

"""
copy.copy() is a shallow copy, changes to box.corner will effect
the other box's.corner. copy provides deepcopy for this:
"""

print('--box3--')
box3 = copy.deepcopy(box)

print(box3 is box) #=> False
print(box3.corner is box.corner) #=> False


def move_rectangle_copy(rect, xmove, ymove):
	copy_rec = copy.deepcopy(rect)
	copy_rec.corner.x += xmove
	copy_rec.corner.y += ymove
	return copy_rec

print_point(box3.corner) #=> (10.5, 10)

box4 = move_rectangle_copy(box3, 10, 10)

print_point(box4.corner) #=> (20.5, 20)
print_point(box3.corner) #=> (10.5, 10)

#debugging
print(type(box)) #=> <class '__main__.Rectangle'>
print(isinstance(box, Rectangle)) #=> True
print(hasattr(box, 'corner')) #=> True
print(hasattr(box, 'doughnut')) #=> False


#exercises 

class Circle:
	"""represents a circle

	attributes: center, radius"""

bob = Circle()
bob.center = Point()
bob.center.x = 150
bob.center.y = 100
bob.radius = 75

print('--exercises--')
print_point(bob.center) #=> (150, 100)

def point_in_circle(circle, point):
	return distance_between_points(circle.center, point) <= circle.radius

#expect False, outside circle
check1 = Point()
check1.x = 20
check1.y = 40

#expect True, inside circle
check2 = Point()
check2.x = 100
check2.y = 50

#expect True, on the line
check3 = Point()
check3.x = 150
check3.y = 25

#expect False, outside circle, close to line
check4 = Point()
check4.x = 150
check4.y = 24.999

print(point_in_circle(bob, check1)) #=> False 	✓
print(point_in_circle(bob, check2)) #=> True 	✓
print(point_in_circle(bob, check3)) #=> True	✓
print(point_in_circle(bob, check4)) #=> False	✓
