'''
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, 
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can 
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.
'''
s = set()
for i in range(2,10):
    for j in range(1000,10000//i):
        p = i*j
        product_set = set((str(i)+str(j)+str(p)))
        if len(product_set) == 9 and '0' not in product_set:
            s.add(p)
            
for i in range(10,100):
    for j in range(100,10000//i):
        p = i*j
        product_set = set((str(i)+str(j)+str(p)))
        if len(product_set) == 9 and '0' not in product_set:
            s.add(p)
print(sum(s))