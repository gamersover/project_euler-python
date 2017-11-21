'''
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
'''
import math

def is_prime(x):
    flag = 1
    if x==1:
        flag = 0
    elif x==2:
        flag = 1
    else:
        for i in range(2,math.ceil(math.sqrt(x))+1):
            if x%i == 0:
                flag = 0
    return flag

def find_prime(x):
    p = []
    i = 2
    while i <= x:
        if is_prime(i):
            p.append(i)
        i+=1
    return p

n = 20
p = find_prime(n)
a = []
for i in p:
    j = math.floor(math.log(n,i))
    a.append(j)
# print(p)
# print(a)
s = 1
for i in range(len(p)):
    s *= p[i]**a[i]
print(s)
