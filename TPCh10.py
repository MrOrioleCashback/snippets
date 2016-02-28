
import random

a = [[1, 2], [3], [4, 5, 6]]	
b = [1, 2, 3]
c = [1, 2, 3, 4, 5, 6, 7, 8]
d = [1, 3, 5, 7, 2, 4, 6, 8]
e = ['a', 'b', 'c', 'd', 'e', 'f', 'b', 'h']


def nested_sum(t):
	return sum(map(sum, t))

#print(nested_sum(a))


def cumsum(t):
	temp = t[:]
	for i in range(1, len(t)):
		temp[i] += temp[i-1]
	return temp	

#print(cumsum(b))


def middle(t):
	temp = t[1:-1]
	return temp

#print(middle(c))	


def chop(t):
	t.pop(0), t.pop(-1)

#print(c)
#print(chop(c))		#return None
#print(c)

def is_sorted(t):
	return True if t == sorted(t) else False

#print(is_sorted(c))
#print(is_sorted(d))


def is_anagram(word1, word2):		#does not deal with punctuation
	if sorted(word1.replace(" ", "").lower()) != sorted(word2.replace(" ", "").lower()):
		return False
	return True	

#print(is_anagram('Debit card', 'Bad credit'))
#print(is_anagram('Dormitory', 'Dirty Room'))
#print(is_anagram('The earthquakes ', 'That queer shake'))
#print(is_anagram('Astronomer', 'Moon starer'))
#print(is_anagram('The eyes', 'They see'))
#print(is_anagram('not an anagram', 'buy trying hard'))


def has_duplicates(t):
	temp = t[:]
	temp.sort()
	for i in range(len(temp)-1):
		if temp[i] == temp[i+1]:
			return True
	return False	

#print(has_duplicates(e))


def birthday(x):		#rough date generator
	list_of_days = []
	for i in range(x):
		list_of_days.append(random.randint(1, 365))
	return sorted(list_of_days)	

#print(birthday(23))

#print(has_duplicates(birthday(23)))


fin = open('words.txt')


def append(file):		#[Finished in 0.2s]
	word_list = []
	for line in file:
		word_list.append(line)
	return(word_list)	
		
#print(append(fin))


def x_equal_to_x_plus_item(file):		#[Finished in 31.6s]
	word_list = []
	for line in file:
		word_list = word_list + [line]
	return(word_list)	
		
#print(x_equal_to_x_plus_item(fin))	


def reverse_pair(file, check_word):
	for line in file:
		word = line.strip()
		if word[::-1] == check_word:
			return word, check_word
	return 0		

#print(reverse_pair(fin, 'live'))


def zip_words(word1, word2):
	return ''.join([char1 + char2 for char1, char2 in zip(word1, word2)])

print(zip_words('shoe', 'cold'))	#schooled


def unzip_word(word):
	return word[::2], word[1::2]

print(unzip_word('schooled'))	#('shoe', 'cold')