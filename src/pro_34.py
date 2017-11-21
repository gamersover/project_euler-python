'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of 
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
from math import factorial
sum_ = 0
for n in range(10,1000000):
    sum_of_digits = 0
    for digit in str(n):
        sum_of_digits += factorial(int(digit))
    if sum_of_digits == n:
        sum_ += n

print(sum_)