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
            inverse[value] = [key]
        else:
            inverse[value].append(key)
    return inverse
    
print(invert_dict(histogram_with_get('parrot')))


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
    print(n, known)
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
