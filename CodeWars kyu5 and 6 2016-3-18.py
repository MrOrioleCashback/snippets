"""
Feynman's squares

Richard Phillips Feynman was a well-known American physicist and a recipient of 
the Nobel Prize in Physics. He worked in theoretical physics and pioneered the 
field of quantum computing.

Recently, an old farmer found some papers and notes that are believed to have 
belonged to Feynman. Among notes about mesons and electromagnetism, there was 
a napkin where he wrote a simple puzzle: "how many different squares are there 
in a grid of NxN squares?".

For example, when N=2, the answer is 5: the 2x2 square itself, plus the four 
1x1 squares in its corners:
"""

def count_squares(n):
    return n * (n + 1) * (2 * n + 1) / 6

#print(count_squares(1)) # =>  1
#print(count_squares(2)) # =>  5
#print(count_squares(3)) # =>  14
#print(count_squares(5)) # =>  55
#print(count_squares(8)) # =>  204
#print(count_squares(15))# => 1240


"""
Write a function called validParentheses that takes a string of parentheses, 
and determines if the order of the parentheses is valid. validParentheses 
should return true if the string is valid, and false if it's invalid.

Examples: 
validParentheses( "()" ) => returns true 
validParentheses( ")(()))" ) => returns false 
validParentheses( "(" ) => returns false 
validParentheses( "(())((()())())" ) => returns true 

All input strings will be nonempty, and will only consist of open 
parentheses '(' and/or closed parentheses ')'
"""

def valid_parentheses(string):
    stack = []
    for item in string:
        if item == '(': #if item in open bracket, append to list
            stack.append(item)
        if item == ')':
            if len(stack) == 0: #closed bracket with empy list means no paired open
                return False
            if stack.pop() != '(': #if popping wrong open bracket type -> False
                return False
    return True if len(stack) == 0 else False

#print(valid_parentheses("  ("))#      False
#print(valid_parentheses(")test"))#    False
#print(valid_parentheses(""))#         True
#print(valid_parentheses("hi())("))#   False
#print(valid_parentheses("hi(hi)()"))# True

"""
solution above was adapted from my Checkio Brackets mission solution published on Feb 7th, 2016:

You are given an expression with numbers, brackets and operators. For this task 
only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]". 
Brackets are used to determine scope or to restrict some expression. If a bracket 
is open, then it must be closed with a closing bracket of the same type. The scope 
of a bracket must not intersected by another bracket. In this task you should make 
a decision, whether to correct an expression or not based on the brackets. Do not 
worry about operators and operands.

Input: An expression with different of types brackets as a string (unicode).

Output: A verdict on the correctness of the expression in boolean (True or False).
"""

def checkio(expression):
    """checks if all open brackets are closed, and no bracket is closed with 
    another bracket 'half-in'"""
    open_bracket = ('({[')
    closed_bracket = (')}]')
    stack = []
    expression = ''.join([char for char in expression if char in ('(){}[]')])   #simplify expression
    
    if len(expression) % 2 != 0:      #quick check for odd # of items in expression
        return False
    for item in expression:
        if item in open_bracket:            #if item in open bracket, append to list
            stack.append(item)
        if item in closed_bracket:
            if len(stack) == 0:     #closed bracket with empy list means no paired open
                return False
            if stack.pop() != open_bracket[closed_bracket.index(item)]:     #if popping wrong open bracket type -> False
                return False
    return True


#print(checkio("((5+3)*2+1)")) #     == True
#print(checkio("{[(3+1)+2]+}")) #    == True
#print(checkio("(3+{1-1)}")) #       == False
#print(checkio("[1+1]+(2*2)-{3/3}")) # == True
#print(checkio("(({[(((1)-2)+3)-3]/3}-3)")) # == False
#print(checkio("2+3")) #             == True

"""
however the list operations are expensive and could be done cheaper with a 
counter since there is only one bracket type.
"""

def valid_parentheses(string):
    counter = 0
    for item in string:
        if item == '(': counter += 1
        if item == ')': counter -= 1
        if not counter: return False
    return True if counter == 0 else False    


#print(valid_parentheses("  ("))#      False
#print(valid_parentheses(")test"))#    False
#print(valid_parentheses(""))#         True
#print(valid_parentheses("hi())("))#   False
#print(valid_parentheses("hi(hi)()"))# True

"""
not sure if "if not counter" is faster or cheaper than "if counter == 0" but I
assume it's cheaper and faster as it's a boolean check rather than an int check.
"""