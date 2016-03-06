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
        
print_directory(directory)        


#http://www.greenteapress.com/thinkpython/code/structshape.py
#Returns a string representation of a set of type strings.
#>>> structshape([[2,3], [5,7], [8,2]])
#'list of 3 list of 2 int
#useful for tracking data type and structure or 
#trying to identify the cause of shape errors 





###################
# Rice U Quiz 6b  #
# Questions 7 & 8 #
###################

def question7(n):
    numbers = range(2, n)
    result = []
    while len(numbers) > 0:
        result.append(numbers.pop(0))
        for index, x in enumerate(numbers):
            if x % result[-1] == 0:
                del numbers[index]
    return len(result)            

#print question7(1000)


def question8():
    slow, fast, year = 1000, 1, 1
    while slow > fast:
        slow *= 1.2
        fast *= 1.4
        year += 1
    return year   
        
#print question8()