import string, random

words = open("Alice's Adventures in Wonderland by Lewis Carroll.txt").read().split('\n')
xwords = open('words.txt').read().split('\n')
emma = open('Emma by Jane Austen.txt').read().split('\n')

def break_book_into_words(book):
	#apostrophes are a problem, don't => dont
	lower_book = ''
	no_punct = {ord(c): None for c in string.punctuation + string.digits}
	for line in book:
		line = line.replace('-', ' ') #hyphenated words are a problem and are removed
		lower_book += (line.translate(no_punct).lower().strip() + ' ')
	return lower_book.split()

#print(sorted(break_book_into_words(words), key=len))


"""
dictonary.setdefault(key, value) does the work of:

if key in dictonary:
    dictonary[key].append(value)
else:
    dictonary[key] = [value]

in 1 line. Use .setdefault() whenever creating a dict
"""


def unique_word_count(word_list):
	#count each use of each word in a list of words
    dict1 = {}
    for word in word_list:
        dict1.setdefault(word, 0) 
        dict1[word] += 1
    return sorted([(value, key) for key, value in dict1.items()],reverse=True) 

#print(unique_word_count(break_book_into_words(emma)))


def make_list_a_dict(word_list):
	#make a list into a hashable dict
	dict1 = {}
	for word in word_list:
		dict1.setdefault(word, 0)
	return dict1
	
#print(make_list_a_dict(xwords))		


def cross_check_words(word_list, check_list):
	#remove words in word_list found in check_list and return result
    dict1 = {}
    for word in word_list:
        if word not in check_list:
            dict1.setdefault(word, 0) 
            dict1[word] += 1
    return sorted([(value, key) for key, value in dict1.items()],reverse=True) 

"""
nested loops with lists is slow
"""

#print(cross_check_words(break_book_into_words(words), xwords)) #[Finished in 27.7s]

"""
it's worth making a list into a dict when nesting loops.
"""
#print(cross_check_words(break_book_into_words(words), make_list_a_dict(xwords))) #[Finished in 0.1s]

#print(len(break_book_into_words(emma))) #total word count
#print(len(unique_word_count(break_book_into_words(emma)))) #total different words


def top_10_words(book, num=10):
	hist = unique_word_count(break_book_into_words(book))
	print('the top %s most common words are:' % num)
	for freq, word in hist[:num]:
		print(word, freq, sep='\t'*2)

#top_10_words(emma)

""" 
#sep='<slash>t'*2 tells python to use two tab seperators rather than a space like so:

the top 10 most common words are:
to		5242
the		5204
and		4897
of		4293
i		3191
a		3130
it		2529
her		2483
was		2400
she		2364

The optional argument 'num=10' defaults to 10 but can be changed when calling the function
optional arguments always follow the required ones.
""" 
