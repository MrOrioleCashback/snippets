def is_palindrome(sequence):
    return sequence == sequence[::-1]
   
def longest_palindromic(text):
    """finds the longest palindromic substring of a given string"""
    longest = ''
    for i in range(len(text)):
        for x in range(len(text) - i):
            if is_palindrome(text[i:len(text) - x]) and\
                len(text[i:len(text) - x]) > len(longest):
                    longest = text[i:len(text) - x]
    return longest    

"""
Write a function that finds the longest palindromic substring 
of a given string. Try to be as efficient as possible!

If you find more than one substring you should return the one 
which is closer to the beginning.

Input: A text as a string.

Output: The longest palindromic substring.

Precondition: 1 < |text| ≤ 20
The text contains only ASCII characters.    
"""

print(longest_palindromic("artrartrt")) #== "rtrartr", "The Longest"
print(longest_palindromic("abacada")) #== "aba", "The First"
print(longest_palindromic("aaaa")) #== "aaaa", "The A"