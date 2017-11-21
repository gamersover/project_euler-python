'''
Starting with the number 1 and moving to the right in a clockwise direction 
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?
'''
all_num = 1001**2

a = 1
i = 1
s = 0
while a <= all_num:
    s += a
    a = a + 2*i
    i += 1

b = 1
i = 1
while b <= all_num:
    s += b
    print(b)
    i += 1
    if i%2 != 0:
        b = i**2
    else:
        b = b + 2*i
    
print(s-1)
