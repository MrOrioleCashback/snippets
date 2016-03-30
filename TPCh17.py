class Time:
	"""
	Represents the time of day
	attributes: Hour, Minute, Second
	"""
	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second

	def __str__(self):
		return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

	def __add__(self, other):
		if isinstance(other, Time):
			return self.add_time(other)
		else:
		    return self.incriment(other)

	def __radd__(self, other):
		return self.__add__(other)	    	

	def time_to_ints(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds

	def add_time(self, other):
		seconds = self.time_to_ints() + other.time_to_ints()
		return ints_to_time(seconds)

	def incriment(self, seconds):
			seconds += self.time_to_ints()
			return ints_to_time(seconds)

	def is_after(self, other):
		return self.time_to_ints() > other.time_to_ints()

def ints_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60) # minutes = seconds // 60 and time.seconds = seconds % 60
	hour, time.minute = divmod(minutes, 60) # hour = minutes // 60 and time.minutes = minutes % 60
	time.hour = hour % 24
	return time


start = Time()
start.hour = 9
start.minute = 45
start.second = 00

end = Time()
end.hour = 10
end.minute = 15
end.second = 0

#start.print_time() #=> 09:45:00

"""
using a function print_time(start) is saying: 

'Hey, print_time, here's an object for you to print'

While in OOP the object is the active agent, start.print_time() says:

'Hey Start, print yourself'
"""

print(start.time_to_ints()) #=> 30137

#start.print_time() #=> 09:45:00
end = start.incriment(1337)
#end.print_time() #=> 10:07:17


print(end.is_after(start)) #=> True


time1 = Time()
#time1.print_time() #=> 00:00:00

time1.hour = 9
#time1.print_time() #=> 09:00:00

time1.minute = 30
#time1.print_time() #=> 09:30:00

"""Lets change print_time() into a print method"""

time1 = Time(8, 20, 45)
print(time1) #=> 08:20:45

"""Lets add an add method so we can add time objects together"""

time2 = Time(0, 14, 15)
print(time1 + time2) #=> 08:35:00

"""For every operator (*, /, %, **, etc...) there is a corresponding special 
method like __add__ that can be used to describe opertator behavior with user
defined classes, this is called Operator Overloading. 
"""

"""Lets modify __add__ so we can incriment seconds or add times depending on 
input. This would make __add__ 'Polymorphic' or give it the ability to work
with more than 1 type
"""

print(time1 + time2) #=> 08:35:00
print(time1 + 625) #=> 08:31:10

"""Problem is when we try and add time to seconds we get an error"""

#print(625 + time1) #=> TypeError: unsupported operand type(s) for +: 'int' and 'Time'

"""We can use 'right-side add': __radd__ for when python detects our time object on the
right side of the '+' operator
"""
print(625 + time1) #=> 08:31:10


"""sum works because our class now supports addition"""

t1 = Time(3, 23, 15)
t2 = Time(1, 15, 39)
t3 = Time(2, 0, 43)

total = sum([t1, t2, t3])

print(total) #=> 06:39:37


"""vars can be helpful in debugging, it returns a dict of attribute values to names"""

print(vars(total)) #=> {'minute': 39, 'hour': 6, 'second': 37}

def print_attributes(obj):
	for attr in vars(obj):
		print(attr, getattr(obj, attr))

print_attributes(total)
    #=> minute 39
    #=> second 37
    #=> hour 6


"""This exercise is a cautionary tale of one of the most common and difficult 
to find errors in python.
"""

class Kangaroo:
	"""docstring for Kangaroo"""
	
	def __init__(self, pouch_contents = []):
		self.pouch_contents = pouch_contents

	def __str__(self):
		return object.__str__(self) + ' ' + str([(attr, getattr(self, attr)) for attr in vars(self)])

	def put_in_pouch(self, item):
		self.pouch_contents.append(item)


kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')


print(kanga) #=> <__main__.Kangaroo object at 0x00330CD0> [('pouch_contents', ['wallet', 'car keys'])]
print(roo) #=> <__main__.Kangaroo object at 0x00330D30> [('pouch_contents', ['wallet', 'car keys'])]


"""The problem is the default value for contents. Default values get 
evaluated ONCE, when the function is defined; they don't get evaluated 
again when the function is called. In this case that means that 
when __init__ is defined, [] gets evaluated and contents gets a 
reference to an empty list.

After that, every Kangaroo that gets the default value get a reference 
to THE SAME list.  If any Kangaroo modifies this shared list, they all 
see the change.

The next version of __init__ shows an idiomatic way to avoid this problem.
"""


class Kangaroo2:
	"""docstring for Kangaroo2"""
	
	def __init__(self, pouch_contents = None):
		if pouch_contents == None:
			pouch_contents = []
		self.pouch_contents = pouch_contents

	def __str__(self):
		return object.__str__(self) + ' ' + str([(attr, getattr(self, attr)) for attr in vars(self)])

	def put_in_pouch(self, item):
		self.pouch_contents.append(item)


kanga2 = Kangaroo2()
roo2 = Kangaroo2()
kanga2.put_in_pouch('pickle')
kanga2.put_in_pouch('deviled egg')


print(kanga2) #=> <__main__.Kangaroo2 object at 0x00620EF0> [('pouch_contents', ['pickle', 'deviled egg'])]
print(roo2) #=> <__main__.Kangaroo2 object at 0x00620F50> [('pouch_contents', [])]