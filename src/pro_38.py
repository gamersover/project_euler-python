'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying 
by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

dict = {2:4, 3:3, 4:2, 5:1, 6:1, 7:1, 8:1, 9:1}

def get_max(s, max_num):
    
    if '0' not in s and len(set(s)) == 9 and len(s) == 9:
        if int(''.join(s)) > max_num:
            max_num = int(''.join(s))
    return max_num
    

max_num = 0


for i in range(1000, 10000):
    a = i
    b = i*2
    s = str(a)+str(b)
    max_num = get_max(s, max_num)

for i in range(100,1000):
    a = i
    b = i*2
    c = i*3
    s = str(a)+str(b)+str(c)
    max_num = get_max(s, max_num)

for i in range(10,100):
    s = ''
    for j in range(1,5):
        s += str(i*j)
    max_num = get_max(s, max_num)

for i in range(1,10):
    s = ''
    for j in range(1,10):
        s += str(i*j)
    max_num = get_max(s, max_num)

print(max_num)