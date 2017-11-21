'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than 
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers 
is 24. By mathematical analysis, it can be shown that all integers greater than 
28123 can be written as the sum of two abundant numbers. However, this upper 
limit cannot be reduced any further by analysis even though it is known that 
the greatest number that cannot be expressed as the sum of two abundant numbers 
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
two abundant numbers.
'''
import math

def get_sum(a):
    s = 0
    for i in range(2,math.floor(math.sqrt(a))+1):
        if a%i == 0 and i != math.sqrt(a):
            s += i
            s += a//i
        elif i == math.sqrt(a):
            s += i
    return s+1

arr = []
for i in range(12,28112):
    if i < get_sum(i):
        arr.append(i)
print(arr)

arr_set = set()
for i in range(len(arr)):
    for j in range(i, len(arr)):
        s = arr[i] + arr[j]
        if s > 28123:
            break
        else:
            arr_set.add(s)
print(sum(range(1,28124))- sum(arr_set))

