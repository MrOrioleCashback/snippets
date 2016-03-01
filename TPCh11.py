list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = [1, 2, 3, 4, 5, 6]
list3 = 'bananna'

my_dict = dict([(x, y) for x, y in zip(list1, list2)])

my_dict['g'] = 7

print(my_dict)  #unordered
print('a' in my_dict)   #indexed by key
print(1 in my_dict)     #only keys
print(1 in my_dict.values())    #use .values() to search values


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
   
print(histogram(list3))        
            
