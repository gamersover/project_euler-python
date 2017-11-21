'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
n = 999
n_3 = n//3
n_5 = n//5
n_15 = n//15
print(n_3,n_5,n_15)
sum_3 = 3*(n_3)*(n_3+1)//2
sum_5 = 5*(n_5)*(n_5+1)//2
sum_15 = 15*(n_15)*(n_15+1)//2
re = sum_3 + sum_5 - sum_15
print(re)