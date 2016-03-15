"""
Write a function that generate the sequence of numbers which starts from the 
"From" number, then adds to each next term the "Step" number until the "To" 
number. For example:

generator(10, 20, 10) = [10, 20] # "From" = 10, "Step" = 10, "To" = 20

generator(10, 20, 1) = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
generator(10, 20, 5) = [10, 15, 20]

If next term is greater than "To", it can't be included into the output array:

generator(10, 20, 7) = [10, 17]

If "From" bigger than "To", the output array should be written in reverse order:

generator(20, 10, 2) = [20, 18, 16, 14, 12, 10]

Don't forget about input data correctness:

generator(20, 10, 0) = []
generator(10, 20, -5) = []

"From" and "To" numbers are always integer, which can be negative or positive 
independently. "Step" can always be positive.
"""


def generator (From, To, Step):
	s = Step if From < To else -Step
	t = 1 if From < To else -1	
	return [] if Step == 0 else [x for x in range(From, To+t, s)]

#print(generator(10, 20, 1))# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#print(generator(20, 10, 1))# [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
#print(generator(10, 20, 0))# []
#print(generator(10, 20, 5))# [10, 15, 20]
#print(generator(0, 1, 1))	# [0, 1]
#print(generator(10, 20, 7))# [10, 17]



"""
While developing a website, you detect that some of the members have troubles 
logging in. Searching through the code you find that all logins ending with 
a "_" make problems. So you want to write a function that takes an array of 
pairs of login-names and e-mails, and outputs an array of all login-name, 
e-mails-pairs from the login-names that end with "_".

If you have the input-array:

[ [ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]

it should output

[ [ "bar_", "bar@bar.com" ] ]

You have to use the filter-method of Python, which returns each element of 
the array for which the filter-method returns true.
"""

def search_names_list_comp(logins):
	return ([x for x in logins if x[0][-1] == '_'])

def search_names(logins):
	return list(filter(lambda x: x[0][-1] == '_', logins))


#print(search_names([[ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ]])) 
					#[[ "bar_", "bar@bar.com"]]
#print(search_names([[ "foobar_", "foo@foo.com" ], [ "bar_", "bar@bar.com" ]])) 
					#[["foobar_", "foo@foo.com"], ["bar_", "bar@bar.com"]]
#print(search_names([[ "foo", "foo@foo.com" ], [ "bar", "bar@bar.com" ]])) 
					# []
