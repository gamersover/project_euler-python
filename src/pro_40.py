'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, 
find the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
'''
import math
def get_dig(n):
    s = 0
    i = 0
    while s < n:
        s += 9*10**i*(i+1)
        i += 1
    
    s = 0
    for j in range(i-1):
        s += 9*10**j*(j+1)
    k = math.ceil((n-s)/i)
    m = 10**(i-1) + k - 1
    q = n - (s + (k-1)*i)
    return int(str(m)[q-1])

re = 1
for i in range(7):
    re *= get_dig(10**i)
print(re)

