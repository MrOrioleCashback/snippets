def checkio(first, second):
    result = []
    for word in first.split(','):
        if word in second.split(','):
            result.append(word)
    return ','.join(sorted(result))

"""
Let's continue examining words. You are given two string with words separated 
by commas. Try to find what is common between these strings. The words are not 
repeated in the same string.

Your function should find all of the words that appear in both strings. The 
result must be represented as a string of words separated by commas in 
alphabetic order.

Input: Two arguments as strings.

Output: The common words as a string.

Example:


print(checkio("hello,world", "hello,earth")) == "hello"
print(checkio("one,two,three", "four,five,six")) == ""
print(checkio("one,two,three", "four,five,one,two,six,three")) == "one,three,two"
"""


