#coding=UTF-8
'''
Starting in the top left corner of a 2*2 grid, and only being able to 
move to the right and down, there are exactly 6 routes to the 
bottom right corner.

How many such routes are there through a 20*20 grid?
'''
'''
设格子形状为 n*m, 从左上角到右下角，总共需要经过n+m条路径，其中必然有n条向下， m条向右走，随便选取那几次
为向下走即可确定唯一的路径, 相当于在n+m中取m条的一共有多少种， 所以结果为C(m+n, n)或C(m+n,m)
'''
#动态规划解法
# N = 20
# dp = [[0 for i in range(N+1)] for i in range(N+1)]
# for i in range(N+1):
#     dp[1][i] = i+1
# for i in range(2,N+1):
#     for j in range(N+1):
#         for k in range(j+1):
#             dp[i][j] += dp[i-1][k]
#  
# print(sum(dp[19][:21]))

#递归解法
# def count_routers(m,n):
#     if m == 0 or n == 0:
#         return 1
#     else:
#         return count_routers(m, n-1) + count_routers(m-1, n)
    
# print(count_routers(14, 14))

#数学公式解法
N = 20
re_1 = 1
re_2 = 1
for i in range(1,21):
    re_1 *= (N+i)
    re_2 *= i
print(re_1//re_2)