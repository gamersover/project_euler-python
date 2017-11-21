'''
You are given the following information, but you may prefer to do some research 
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,April, June and November.
All the rest have thirty-one,Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century 
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth 
century (1 Jan 1901 to 31 Dec 2000)?
'''

init_day = 6
s = 0
for i in range(1901,2001):
    for j in range(1,13):
        if j == 3:
            if i%4 == 0:
                init_day += 29%7
            else:
                init_day += 28%7
        elif j == 5 or j == 7 or j == 10 or j == 12:
            init_day += 30%7
        else:
            init_day += 31%7
        init_day = init_day%7
        if init_day == 0:
            s += 1

        print(init_day)
print(s)