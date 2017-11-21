'''
A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91*99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
def is_palindormic(n):
    arr = [int(i) for i in str(n)]
    a = arr.copy()
    a.reverse()
    v = list(map(lambda x: x[0]^x[1], zip(arr, a)))
    if sum(v) == 0:
        return 1
    else:
        return 0

a = 999
max = 0
while a >= 100:
    if a%11 ==0:
        b = 999
        db = 1
    else:
        b = 990
        db = 11
    
    while b < a and b>=100:
        n = b*a
        if is_palindormic(n):
            if n > max:
                max = n
        b -= db
    a -= 1
print(max)
 
        