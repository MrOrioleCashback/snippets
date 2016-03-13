import string

words = open("Alice's Adventures in Wonderland by Lewis Carroll.txt").read().split('\n')
xwords = open('words.txt').read().split('\n')

def break_book_into_words(book):
	lower_book = ''
	no_punct = {ord(c): None for c in string.punctuation + string.digits}
	for line in book:
		line = line.replace('-', ' ') #hyphenated wirds are a problem
		lower_book += (line.translate(no_punct).lower().strip() + ' ')
	return lower_book.split()

#print(sorted(break_book_into_words(words), key=len))


def unique_word_count(word_list):
    dict1 = {}
    for word in word_list:
        dict1.setdefault(word, 0) 
        dict1[word] += 1
    return sorted([(value, key) for key, value in dict1.items()],reverse=True) 


#print(unique_word_count(break_book_into_words(words)))


def cross_check_words(word_list, check_list):
    dict1 = {}
    for word in word_list:
        if word not in check_list:
            dict1.setdefault(word, 0) 
            dict1[word] += 1
    return sorted([(value, key) for key, value in dict1.items()],reverse=True) 

#print(cross_check_words(break_book_into_words(words)))
