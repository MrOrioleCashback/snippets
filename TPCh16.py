class Time:
	"""
	Represents the time of day
	attributes: Hour, Minute, Second
	"""

time = Time()
time.hour = 8
time.minute = 0
time.second = 0

def print_time(time):
	"""the format sequence '%.2d' prints an intiger with at least 2 digits
	including a leading '0' if nessassary"""
	print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

print_time(time) #=> 08:59:30

def is_after(time1, time2):
	"""check if time1 is after time2
	*bonus: don't use an 'if' statement
	"""
	t1 = (time1.hour * 10000) + ((time1.minute+1) * 100) + time1.second
	t2 = (time2.hour * 10000) + ((time2.minute+1) * 100) + time2.second
	return t1 > t2


time2 = Time()
time2.hour = 7
time2.minute = 59
time2.second = 59

print(is_after(time, time2)) #=> True


"""
adding time
"""

def add_time(t1, t2):
	sumtime = Time()
	sumtime.hour = t1.hour + t2.hour
	sumtime.minute = t1.minute + t2.minute
	sumtime.second = t1.second + t2.second
	return time_increment(sumtime)

def time_increment(time):
	#corrects time addition format errors
	while time.second > 60:
		time.second -= 60
		time.minute += 1

	while time.minute > 60:
		time.minute -= 60
		time.hour += 1

	if time.hour > 24:
		time.hour %= 24

	return time	


"""
lets find out when a movie will be done
"""

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print_time(done) #=> 11:20:00

"""
improperly formated minutes
"""

race_start = Time()
race_start.hour = 9
race_start.minute = 45
race_start.second = 0

race_duration = Time()
race_duration.hour = 0
race_duration.minute = 90 #imporperly formated 
race_duration.second = 0

race = add_time(race_start, race_duration)
print_time(race) #=> 11:15:00

"""
all of this can be done eaiser, break time into seconds and return to proper format
"""

def time_to_ints(time):
	minutes = time.hour * 60 + time.minute
	seconds = minutes * 60 + time.second
	return seconds

def ints_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60) # minutes = seconds // 60 and time.seconds = seconds % 60
	hour, time.minute = divmod(minutes, 60) # hour = minutes // 60 and time.minutes = minutes % 60
	time.hour = hour % 24
	return time

def add_time2(t1, t2):
	time = time_to_ints(t1) + time_to_ints(t2)
	return ints_to_time(time)

done_again = add_time2(start, duration)
print_time(done_again) #=> 11:20:00
race_again = add_time2(race_start, race_duration)
print_time(race_again) #=> 11:15:00


"""
exercises
"""

def time_per_mile(time, miles):
	"""
	returns average minutes per mile
	"""
	return ints_to_time(time_to_ints(time) / miles)


my_time = Time()
my_time.hour = 2
my_time.minute = 13
my_time.second = 42

print_time(time_per_mile(my_time, 20)) # => 00:06:41 (not bad!)


import datetime


def what_day_is_it():
    now = datetime.datetime.now()
    print(now.strftime("%A"))

what_day_is_it() # => Sunday


def days_diff(date1, date2):
    datetime1 = datetime.date(date1[0], date1[1], date1[2])
    datetime2 = datetime.date(date2[0], date2[1], date2[2])
    try:
        return abs(int(str(datetime1 - datetime2).split()[0]))
    except ValueError:
        return 0

def birthday(year, month, day):
	now = str(datetime.datetime.now()).split('-')
	print("It's %d days until your birthday" % days_diff((int(now[0]), int(now[1]), int(now[2][:2])), (int(now[0]), month, day)))
	print("You're %d years old" % (days_diff((int(now[0]), int(now[1]), int(now[2][:2])), (year, month, day)) / 365))

birthday(1900, 1, 1)	
