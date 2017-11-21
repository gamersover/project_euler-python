'''
A permutation is an ordered arrangement of objects. For example, 
3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import math

num = 1000000
re = []
arr = [0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    
    a = math.factorial(9-i)
    re.append(arr[num//a])
    del arr[num//a]
    num %= a
print(re)
"re is 2783915604"
"re's last permutation  in the result"
"so the result is 2783915460"