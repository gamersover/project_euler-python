'''
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and 
is also prime.

What is the largest n-digit pandigital prime that exists?
'''
import math
from itertools import permutations

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

for i in reversed(list(permutations('1234567'))):
    n = int(''.join(i))
    if is_prime(n):
        print(n)
        break

        