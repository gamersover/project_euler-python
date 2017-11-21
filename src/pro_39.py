'''
If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''
from collections import Counter
p = []
for i in range(1,251):
    for j in range(i+1, 501-i):
        for k in range(j+1,i+j):
            if i**2 + j**2 == k**2:
                a = i+j+k
                p.append(a)
print(p)

print(Counter(p).most_common())