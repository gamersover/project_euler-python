'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
import math
a = 600851475143
flag = 0
while 1:
    n = math.ceil(math.sqrt(a))
    for i in range(2,n+1):
        if a%i == 0:
            a = a//i
            break
        elif i == n:
            flag = 1
            print(a)
    if flag==1:
        break    
        
        