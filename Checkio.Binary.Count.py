def checkio(num):
    return len([x for x in bin(num) if x is '1'])

#Remember methods like .count()

"""
For the Robots the decimal format is inconvenient. If they need to count to
 "1", their computer brains want to count it in the binary representation of
  that number. You can read more about binary here.

You are given a number (a positive integer). You should convert it to the
 binary format and count how many unities (1) are in the number spelling. 
 For example: 5 = 0b101 contains two unities, so the answer is 2.

Input: A number as a positive integer.

Output: The quantity of unities in the binary form as an integer.


print(checkio(4)) == 1
print(checkio(15)) == 4
print(checkio(1)) == 1
print(checkio(1022)) == 9
"""