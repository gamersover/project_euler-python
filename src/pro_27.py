'''
Euler discovered the remarkable quadratic formula:

                        n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive 
integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is divisible 
by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79*n+1601 was discovered, which produces 80 primes 
for the consecutive values 0≤n≤79. The product of the coefficients,
 −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, 
starting with n=0.
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
    
prime_arr = [i for i in range(1,1000) if is_prime(i)]

max_n = 0
for b in prime_arr:
    for a in range(1-b, 1000):
        n = 0
        while n**2+a*n+b > 0 and is_prime(n**2+a*n+b):
            n += 1
        if n > max_n:
            max_a = a
            max_b = b
            max_n = n
print(max_a, max_b, max_a*max_b, max_n)