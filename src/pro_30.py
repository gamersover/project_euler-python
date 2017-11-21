'''
Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of 
fifth powers of their digits.
'''
import math

# i = 1
# a = (10**(i) - 1)//9
# b = i*(9**5)
# while a <= b:
#     i += 1
#     a = (10**(i) - 1)//9
#     b = i*(9**5)
re = 0
for num in range(4000,1000000):
    if num == sum(map(lambda x:int(x)**5,str(num))):
        re += num
print(re)   
    