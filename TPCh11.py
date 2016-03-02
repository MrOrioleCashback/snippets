list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = [1, 2, 3, 4, 5, 6]
list3 = 'bananna'

my_dict = dict([(x, y) for x, y in zip(list1, list2)])

my_dict['g'] = 7

#print(my_dict)  #unordered
#print('a' in my_dict)   #indexed by key
#print(1 in my_dict)     #only keys
#print(1 in my_dict.values())    #use .values() to search values


def histogram(string):
    temp_dict = dict()
    for character in string:
        if character not in temp_dict:
            temp_dict[character] = 1
        else:
            temp_dict[character] += 1
    return temp_dict
   
#print(histogram(list3))

#print(my_dict.get('x', 5))


def histogram_with_get(string):
    temp_dict = dict()
    for character in string:
        temp_dict[character] = temp_dict.get(character, 0) + 1
    return temp_dict       

#print(histogram_with_get(list3))


def print_hist(dic):
    for character in dic:
        print(character, dic[character])

#print_hist(my_dict)
#print('----------------')


def print_hist_sorted(dic):
    for character in sorted(dic):
        print(character, dic[character])

#print_hist_sorted(my_dict) 
#print('----------------')


def reverse_lookup(dic, value):
    for key in dic:
        if dic[key] == value:
            return key
    raise LookupError('Value not in dictonary')
    
#print(reverse_lookup(my_dict, 8))


def invert_dict(dic):
    inverse = dict()
    for key in dic:
        value = dic[key]
        if value not in inverse:
            inverse[value] = key
        else:
            inverse[value].append(key)
    return inverse
    
#print(invert_dict(histogram_with_get('parrot')))


def fabonacci(n):
    """
    Return the n'th number of the fabonacci sequence
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabonacci(n-1) + fabonacci(n-2)

#print(fabonacci(40)) #[Finished in 64.7s]


known = {0:0, 1:1}

def fabonacci_with_memo(n):
    if n in known:
        return known[n]
    result = fabonacci_with_memo(n-1) + fabonacci_with_memo(n-2)
    known[n] = result
    return result

#print(fabonacci_with_memo(40)) #[Finished in 0.1s]


count = 0

def counter():
    count += 1
    return(count)

#print(counter()) #UnboundLocalError: local variable 'count' referenced before assignment

def counter_global():
    global count
    count += 1
    return(count)

#print(counter_global())    



#----------------------------------------------------------
fin = open('words.txt')




def word_dict_search(file, search_word):
    word_keys = dict()
    for line in file:
        word = line.strip()
        word_keys[word] = 0
    if search_word in word_keys:
        return True
    return False

#print(word_dict_search(fin, 'zamindars'))   #[Finished in 0.1s]
  

def list_search(file, search_word):
    word_list = []
    for line in file:
        word = line.strip()
        word_list.append(word)
    if search_word in word_list:
        return True
    return False
        
#print(list_search(fin, 'zamindars'))    #[Finished in 0.1s]


def inverse_with_setdefault(dic):
    inverse = dict()
    for key in dic:
        value = dic[key]
        inverse.setdefault(value, key)
    return inverse

#print(invert_dict(my_dict))   
#print(inverse_with_setdefault(my_dict))   


def ackermann(m, n):
    """
    http://en.wikipedia.org/wiki/Ackermann_function
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))

#print(ackermann(3, 4))


e = ['a', 'b', 'c', 'd', 'e', 'f', 'b', 'h']

def has_duplicates(t):
    #list version
    temp = t[:]
    temp.sort()
    for i in range(len(temp)-1):
        if temp[i] == temp[i+1]:
            return True
    return False    

#print(has_duplicates(e))


def has_duplicates_dict(t):
    temp_dict = dict()
    for item in t:
        if item in temp_dict:
            return True
        temp_dict[item] = 1
    return False            

#print(has_duplicates_dict(e))


def wordlist_dict(file):
    word_keys = dict()
    for line in file:
        word = line.strip()
        word_keys[word] = 0
    return word_keys


def rotate_pairs(word, file):
    rotated = word[::-1].lower()
    if word in wordlist_dict(file):
        return word, rotated
    return 'not found'    

#print(rotate_pairs('pots', fin))      
