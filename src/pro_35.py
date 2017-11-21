'''
The number, 197, is called a circular prime because all rotations of the digits: 
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 
73, 79, and 97.
How many circular primes are there below one million?
'''
import math
def is_prime(x):
    if x==1:
        return False
    elif x < 4:
        return True
    elif x % 2 == 0:
        return False
    elif x < 9:
        return True
    elif x%3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(x))
        f = 5
        while f <= r:
            if x % f == 0:
                return False
            if x % (f+2) == 0:
                return False
            f += 6
        return True
    
def rotate_num(num):
    rotate_li = []
    dig_li = str(num)
    for i in range(len(dig_li)):
        rot_n = dig_li[i:] + dig_li[:i]
        rotate_li.append(int(rot_n))
    return rotate_li
        
total_num = 1000000
not_set = set()
prime_li = []
for i in range(1,total_num):
    flag = 0
    rotate_i = rotate_num(i)
    for j in range(len(rotate_i)):
        if not is_prime(rotate_i[j]):
            flag=1
            break
    if flag:
        not_set.add(i)

result_set = set(range(1,1000000)) - not_set
print(result_set)
print(len(result_set))
    
    
        