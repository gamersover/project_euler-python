'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
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

n = 2000000
s = 5
k = 5
while k < n:
    if is_prime(k):
        s += k
    k += 2
    if k < n and is_prime(k):
        s += k
    k += 4
print(s)