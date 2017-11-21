'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.
What is the 10 001st prime number?
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

n = 10001

i = 0
j = 1
while i < n:
    if is_prime(j):
        i += 1
    j += 1
print(j-1)
# print(is_prime(45))