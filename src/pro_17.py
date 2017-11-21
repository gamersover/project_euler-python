'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 
(three hundred and forty-two) contains 23 letters and 
115 (one hundred and fifteen) contains 20 letters. The use of "and" when 
writing out numbers is in compliance with British usage.
'''
count_1 = 3
count_2 = 3
count_3 = 5
count_4 = 4
count_5 = 4
count_6 = 3
count_7 = 5
count_8 = 5
count_9 = 4
count_10 = 3
count_11 = 6
count_12 = 6
count_13 = 8
count_14 = 8
count_15 = 7
count_16 = 7
count_17 = 9
count_18 = 8
count_19 = 8
count_20 = 6
count_30 = 6
count_40 = 5
count_50 = 5
count_60 = 5
count_70 = 7
count_80 = 6
count_90 = 6
count_00 = 7
count_000 = 8
count_and = 3

s = 191 * count_1 + 190 * (count_2+count_3+count_4+count_5+count_6+count_7+count_8+count_9) + 10*(count_10+count_11+count_12+count_13+count_14+count_15+count_16+count_17+count_18+count_19) +  100*(count_20+count_30+count_40+count_50+count_60+count_70+count_80+count_90) + 900 *count_00 + count_000 + 891 * count_and
print(s)