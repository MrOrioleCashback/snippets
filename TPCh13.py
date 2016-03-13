import string

words = open("Alice's Adventures in Wonderland by Lewis Carroll.txt").read().split('\n')

def break_book_into_words(book):
	lower_book = ''
	no_punct = {ord(c): None for c in string.punctuation + string.digits}
	for line in book:
		lower_book += (line.translate(no_punct).lower().strip() + ' ')
	return lower_book.split()

print(break_book_into_words(words))