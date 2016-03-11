"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 
below the number passed in.
"""

def solution(number):
  return sum([x for x in range(0, number) if x % 5 == 0 or x % 3 == 0])


"""
Write a function that takes in a string of one or more words, and returns the 
same string, but with all five or more letter words reversed (Just like the 
name of this Kata). Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
"""

def spin_words(sentence):       #1st solution
    for word in sentence.split():
        if len(word) >= 5:
            sentence = sentence.replace(word , word[::-1])
    return sentence

def spin_words(sentence):       #2nd solution
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])
    #'else word' logic remains on the left of the 'for word in sentence'


"""
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

double_char("String") ==> "SSttrriinngg"
double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
double_char("1234!_ ") ==> "11223344!!__  "
"""

def double_char(s):
    return ''.join([x*2 for x in s])