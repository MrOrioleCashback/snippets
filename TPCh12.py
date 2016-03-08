c = 'cat'
d = 'dog'

c, d = d, c

#print(c, d)


address = 'monty@python.org'

username, domain = address.split('@')

#print(username, domain)


def minmax(t):
    return min(t), max(t)
    
#print(minmax((1,2,3,4,5,6)))


def printall(*args):
    print(args)
    
#printall(2,{5:'h', 'y':'frog'},[3,6],'g', 'd', (5, 3, 7), 'Bananna')


def sumall(*args):
    return sum([x for x in args])
    
#print(sumall(5,6,7,8,9))


s = 'abc'
t = (1, 2, 3)

def zip_print(x, y):
    for pair in zip(x, y):
        print(pair)
        
#zip_print(s, t)


z = list(zip(s, t))
#print(z)


def print_elements(seq):
    for x, y, in seq:
        print(x, y)
        
#print_elements(z)        


e = ('s', 'o', 'c', 'u')
f = ('m', '3', 'c', 'x')


def has_match(t1, t2):
    for x, y, in zip(t1, t2):
        if x == y:
            return True
    return False
    
#print(has_match(e, f))


g = dict(zip(e, f))
h = dict(zip('abcde', range(5)))

#print(g)
#print(g.items())

#print(h)
#print(h.items())


directory = {('Smith', 'John'): 2125555555,  ('Garcia','Maria'): 2135555555,  
    ('Smith','Mary'): 3125555555,  ('Johnson','James'): 2025555555, 
    ('Hernandez', 'Joe'): 4155555555}

directory[('Jackson', 'Marcus')] = 6175555555

def print_directory(d):
    for last, first in d:
        print(first, last, d[last, first])
        
#print_directory(directory)        


#http://www.greenteapress.com/thinkpython/code/structshape.py
#Returns a string representation of a set of type strings.
#>>> structshape([[2,3], [5,7], [8,2]])
#'list of 3 list of 2 int
#useful for tracking data type and structure or 
#trying to identify the cause of shape errors 

words = open('words.txt').read().split('\n')


def anagram_finder(word_list):
    dict1 = {}
    for word in word_list:
        keyword = tuple(sorted(word))
        if keyword in dict1:
            dict1[keyword].append(word)
        else:
            dict1[keyword] = [word]
    return sorted(dict1.values(), key=len, reverse=True)
    
#print(anagram_finder(words))


def scrabble_bingo(word_list):
    dict1 = {}
    for word in word_list:
        if len(word) == 8:
            keyword = ''.join(sorted(word))
            if keyword in dict1:
                dict1[keyword].append(word)
            else:
                dict1[keyword] = [word]       
    return max(dict1.values(), key=len)

#print(scrabble_bingo(words))			


def metathesis_anagram_potentials(word_list):
    dict1 = {}
    for word in word_list:
        keyword = tuple(sorted(word))
        if keyword in dict1:
            dict1[keyword].append(word)
        else:
            dict1[keyword] = [word]
    return [x for x in dict1.values() if len(x)>1]  

def metathesis_checker(anagram_list):
	list1 = []
	for collection in anagram_list:
		for word1 in collection:
			for word2 in collection:
				counter = 0
				for a, b in zip(word1, word2):
					if a != b and counter < 3:
						counter += 1
				if counter == 2:
					if (word2, word1) not in list1:
						list1.append((word1, word2))
	return sorted(list1)

#print(metathesis_checker(metathesis_anagram_potentials(words)))

"""
What is the longest English word, that remains a valid English word, as you 
remove its letters one at a time?
Now, letters can be removed from either end, or the middle, but you can’t 
rearrange any of the letters. Every time you drop a letter, you wind up with 
another English word. If you do that, you’re eventually going to wind up with 
one letter and that too is going to be an English word—one that’s found in the 
dictionary. I want to know what’s the longest word and how many letters does 
it have?
I’m going to give you a little modest example: Sprite. Ok? You start off with 
sprite, you take a letter off, one from the interior of the word, take the r 
away, and we’re left with the word spite, then we take the e off the end, we’re 
left with spit, we take the s off, we’re left with pit, it, and I.

Write a program to find all words that can be reduced in this way, and then find 
the longest one.
"""

def letter_chipper_boolen(word):
	if len(word) == 1:
		return word in words	
	for n in range(len(word)):
		chipped_word = (word[:n] + word[(n+1):])
		if chipped_word in words:
			return letter_chipper_boolen(chipped_word)
	return False			

def letter_chipper(word):
	if len(word) == 1:
		return word
	for n in range(len(word)):
		chipped_word = (word[:n] + word[(n+1):])
		if chipped_word in words:
			return word, letter_chipper(chipped_word)

def cartalk_recursive_words(word_list):
	for word in sorted(word_list, key=len, reverse=True): #check longest words first
		if letter_chipper_boolen(word): #first True word encountered is returned
			return letter_chipper(word) 

print(cartalk_recursive_words(words))

"""
>>>
('complecting', ('completing', ('competing', ('compting', 
('comping', ('coping', ('oping', ('ping', ('pig', ('pi', 'i'))))))))))
"""
