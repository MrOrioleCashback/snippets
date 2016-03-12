"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels 
from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new 
string with all vowels removed.

For example, the string "This website is for losers LOL!" would become 
"Ths wbst s fr lsrs LL!".
"""

def disemvowel(string):
    return ''.join(x for x in string if x.lower() not in ('a', 'e', 'i', 'o', 'u'))


"""
Welcome. In this kata you are required to, given a string, replace every 
letter with its position in the alphabet. If anything in the text isn't a 
letter, ignore it and don't return it. a being 1, b being 2, etc. As an example:

alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" 
(As a string.)
"""

def alphabet_position(text):
    return ' '.join([str(ord(x.lower()) -96) for x in text if x.isalpha()])
