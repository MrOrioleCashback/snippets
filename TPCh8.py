def reverse_print_for(word):
	reversed_word = ''
	for letter in reversed(word):
		reversed_word += letter
	print(reversed_word)	

reverse_print_for('banannafor')		


def reverse_print(word):
	print(word[::-1])

reverse_print('bananna')


def is_palindrome(sequence):
	return sequence.lower() == sequence[::-1].lower()

print(is_palindrome('Bowling'))


def duckling_names():
	prefix = ['J','K','L','M','N','Ou','P','Qu']
	suffix = 'ack'
	for letter in prefix:
		print(letter+suffix)

duckling_names()


def find(word, letter, startindex):
	index = startindex
	while index < len(word):
		if word[index] == letter:
			return index
		index += 1
	return -1
	
print(find('ramalamadingdong', 'i', 5))


print('ramalamadingdong'.find('i')) 	# str.find(str, start, end)


def how_many_instances(word, letter):
	count = 0
	for digit in word:
		if digit == letter:
			count += 1 
	return count
			
print(how_many_instances('bananna', 'n'))


print('bananna'.count('n')) 	# str.count(str, start, end)


def in_both(word1, word2):
	for letter in word1:
		if letter in word2:
			print(letter)

in_both('apples', 'oranges')


def which_word_first(word1, word2):
	if word1.lower() < word2.lower():
		print(word1, 'comes before', word2)
	else:
	    print(word2, 'comes before', word1)

which_word_first('Bear', 'aligator')


def is_reversed(word1, word2):
	if len(word1) != len(word2):
		return False
	for index, letter in enumerate(word1):
		if letter.lower() != word2[(index + 1) * -1].lower():
			return False
	return True


print(is_reversed('pots', 'Stop'))		

print('0000000Get rid of all the damn zeros!0000000'.strip('0')) 			# str.strip([chars]);
print('xxxxxxxxxxxxxxxGet rid of all the x at the beginning'.lstrip('x')) 	# str.lstrip([chars])	
print('Get rid of all the x at the end!xxxxxxxxxxxxxxxxxxxx'.rstrip('x')) 	# str.rstrip([chars])

print('I love apples, apples are the best, but nothing beats an apple'.replace('apples', 'oranges')) # str.replace(old, new[, max])


def caeser_cypher(word, key):
	"""
	fails for some key range and letter combos, TODO: Find ord() 
	dictionary(?) and adjust ranges to properly wrap.
	"""
	cypher_word = ''
	for letter in word:
		cypher_word += (chr(ord(letter) + key))
	return cypher_word	

print(caeser_cypher('cheer', 7))
