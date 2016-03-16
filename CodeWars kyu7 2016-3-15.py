"""
Instructions

Write a function that takes a single string (word) as argument. The function 
must return an ordered list containing the indexes of all capital letters in 
the string.
"""

def capitals(word):
	return [index for index, letter in enumerate(word) if letter.isupper()]

#print(capitals('CodEWaRs')) # [0,3,4,6]


"""
You have been employed by the Japanese government to write a function that 
tests whether or not a building is strong enough to withstand a simulated 
earthquake.

A building will fall if the magnitude of the earthquake is greater than the 
strength of the building.

An earthquake takes the form of a 2D-Array. Each element within the 
Outer-Array represents a shockwave, and each element within the Inner-Arrays 
represents a tremor. The magnitude of the earthquake is determined by the 
product of the values of its shockwaves. A shockwave is equal to the sum of 
the values of its tremors.

Example --> [[5,3,7],[3,3,1],[4,1,2]] ((5+3+7) * (3+3+1) * (4+1+2)) = 735

A building begins with a strength value of 1000 when first built, but this 
value is subject to exponential decay of 1% per year. For more info on 
exponential decay, follow this link - 
https://en.wikipedia.org/wiki/Exponential_decay

Given an earthquake and the age of a building, write a function that returns 
"Safe!" if the building is strong enough, or "Needs Reinforcement!" if it falls.
"""

def strong_enough( earthquake, age ):
	total, strength = 1, 1000 * 0.99 ** age
	for x in [sum(x) for x in earthquake]:
		total *= x
	return "Safe!" if strength > total else "Needs Reinforcement!"


#print(strong_enough([[2,3,1],[3,1,1],[1,1,2]], 2))#, "Safe!")
#print(strong_enough([[5,8,7],[3,3,1],[4,1,2]], 2))#, "Safe!")
#print(strong_enough([[5,8,7],[3,3,1],[4,1,2]], 3))#, "Needs Reinforcement!")