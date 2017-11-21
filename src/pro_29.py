#coding=UTF-8
'''
Consider all integer combinations of a^b for 2 <= a <= 5 and 2 <= b <= 5:

2^2=4, 2^3=8, 2^4=16, 2^5=32
3^2=9, 3^3=27, 3^4=81, 3^5=243
4^2=16, 4^3=64, 4^4=256, 4^5=1024
5^2=25, 5^3=125, 5^4=625, 5^5=3125
If they are then placed in numerical order, with any repeats removed, 
we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by a^b for 2 <= a <= 100 
and 2 <= b <= 100?
'''
import math

# def get_factor(a,b,arr):
#      
#     if (a,b) in arr:
#         s = 0
#     else:
#         s = 1
#     _max = min(math.floor(math.log(100, a))+1,b)
#     for i in range(2, _max):
#         if b%i == 0:
#             if (a**i, b//i) not in arr:
#                 arr.append((a**i, b//i))
#     return s,arr
#  
# arr = []
# s_all = 0
# for i in range(2,101):
#     for j in range(2,101):
#         s, arr = get_factor(i,j,arr)
#         s_all += s
# print(s_all)
s = 0
for i in range(2,11):
    for j in range(2,8):
        if i**j <= 100:
            s += 100//j - 1
s = 99*99 - s + 1
print(s)