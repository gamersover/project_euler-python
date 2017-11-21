'''
The number 3797 has an interesting property. Being prime itself, it is possible 
to continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, 
and 3.

Find the sum of the only eleven primes that are both truncatable from 
left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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
    
def getNumSet(num):
    num_set = set()
    s = str(num)
    for i in range(len(s)):
        left =  ''.join(s[i:])
        right = ''.join(s[:i+1])
        num_set.add(int(left))
        num_set.add(int(right))
    return num_set

def isAllprime(num):
    arr = list(getNumSet(num))
    for i in arr:
        if not is_prime(i):
            return False
    return True
            

s = []
i = 10
while len(s) < 11:
    if isAllprime(i):
        s.append(i)
        print(i)
    i += 1
print(sum(s))