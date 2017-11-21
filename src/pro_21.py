'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than 
n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair 
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import math

def get_div_sum(a):
    sum_re = 0
    for i in range(2,math.floor(math.sqrt(a))+1):
        if a%i == 0 and i!=math.sqrt(a):
            sum_re += i+a//i
        elif i == math.sqrt(a):
            sum_re += i
    sum_re += 1
    return sum_re

num_set = set()
for a in range(1,10000):
    b = get_div_sum(a)
    if a == get_div_sum(b) and a != b:
        num_set.add(a)
        num_set.add(b)
print(sum(num_set))