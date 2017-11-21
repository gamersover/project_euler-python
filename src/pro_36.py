'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base
10 and base 2.

(Please note that the palindromic number, in either base, 
may not include leading zeros.)
'''

def isHuiWen(num):
    
    li = ''.join(reversed(list(str(num))))
    if li == str(num):
        return True
    else:
        return False

def isPalin(num):

    if isHuiWen(num) and isHuiWen(bin(num)[2:]):
        return True
    else:
        return False

def getSum():
    
    s = 0
    for i in range(1000000):
        if isPalin(i):
            s += i
    return s

print(getSum())