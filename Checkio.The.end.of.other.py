def checkio(words_set):
    for word1 in words_set:
        for word2 in words_set:
            if is_at_end(word1, word2):
                return True
    return False            

def is_at_end(word1, word2):
    """checks if word1 is at the end of word2"""
    return word1 != word2 and word1 == word2[-len(word1):]

"""
Checkio: The end of other
http://www.checkio.org/mission/end-of-other/

In this task, you are given a set of words in lower case. Check 
whether there is a pair of words, such that one word is the end 
of another (a suffix of another). 
For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello", 
so the result is True.

Input: Words as a set of strings.

Output: True or False, as a boolean.

Example:

checkio({"hello", "lo", "he"}) == True
checkio({"hello", "la", "hellow", "cow"}) == False
checkio({"walk", "duckwalk"}) == True
checkio({"one"}) == False
checkio({"helicopter", "li", "he"}) == False
"""
