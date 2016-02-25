
def has_no_e(word):
	return False if 'e' in word else True	

#print(has_no_e('bananna'))


def avoids(word, string):
	for character in string:
		if character in word:
			return False
	return True

#print(avoids('pumpkin', 'sde'))


def uses_only(word, string):
	for character in word:
		if character not in string:
			return False
	return True		

#print(uses_only('bookworm', 'bkwrm')) 


def uses_all(word, string):
	for character in string:
		if character not in word:
			return False
	return True

#print(uses_all('bookworm', 'bkwrm'))


def is_abecedarian(word):
	for index, character in enumerate(word):
		if index < len(word)-1:
			if character > word[index + 1]:
				return False
	return True
	
#print(is_abecedarian('loopy'))			


def three_consecutive_pairs(word):
	for index, letter in enumerate(word):
		if index + 5 < len(word)-1:
			if letter == word[index+1] and word[index+2] == word[index+3] and word[index+4] == word[index+5]:
				return True
	return False

#print(three_consecutive_pairs('mississippi'))	




#---------------File versions-------------




fin = open('words.txt')


def has_no_letter_f(file, letter):
	word_count = 0
	no_letter = 0
	for line in file:
		word_count += 1
		if letter not in line:
			no_letter += 1
			print(line.strip())
	return str(round(no_letter / word_count, 4) * 100) + "% of the words have no", letter

#print(has_no_letter_f(fin, 'e'))


def avoids_f(file, string):
	total_words = 0
	for line in file:
		flag = True
		for character in string:
			if character in line:
				flag = False
		if flag:
			total_words += 1 
			print(line.strip())
	return total_words

#print(avoids_f(fin, 'aeiouy'))


def uses_only_f(file, string):
	total_words = 0
	for line in file:
		flag = True
		word = line.strip()
		for character in word:
			if character not in string:
				flag = False
		if flag:
			total_words += 1 
			print(word)
	return total_words

#print(uses_only_f(fin, 'cat'))


def uses_all_f(file, string):
	total_words = 0
	for line in file:
		flag = True
		word = line.strip()
		for character in string:
			if character not in word:
				flag = False
		if flag:
			total_words += 1 
			print(word)
	return total_words

#print(uses_all_f(fin, 'aeiouy'))	


def abecedarian_f(file):
	total_words = 0
	for line in file:
		flag = True
		word = line.strip()
		for index, character in enumerate(word):
			if index < len(word)-1:
				if character > word[index + 1]:
					flag = False
		if flag:
			total_words += 1 
			print(word)
	return total_words

#print(abecedarian_f(fin))


def three_consecutive_pairs_f(file):
	for line in file:
		word = line.strip()
		if three_consecutive_pairs(word):
			print(word)

#three_consecutive_pairs_f(fin)


def palindromic_odometer():
	"""http://www.cartalk.com/content/palindromic-odometer"""
	for number in range(100000, 999999):
		if is_palindrome(number, 2, 6):
			number += 1
			if is_palindrome(number, 1, 6): 
				number += 1
				if is_palindrome(number, 1, 5):
					number += 1		
					if is_palindrome(number, 0, 6):
						print(number-3)			

def is_palindrome(sequence, start, end):
	sequence = str(sequence)[start:end]
	return sequence == sequence[::-1]

#palindromic_odometer()