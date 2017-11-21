'''
The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2; 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to 
its alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word 
a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), 
a 16K text file containing nearly two-thousand common English words, 
how many are triangle words?
'''

with open('pro_42.txt', 'r') as f:
    line = f.read()

words = map(eval, line.split(','))
get_num = lambda i:ord(i) - 64
word_value = [sum(map(get_num, word)) for word in words]
max_value = max(word_value)

tri_values = []
i = 1
while True:
    v = i*(i+1)//2
    if v > max_value:
        break
    tri_values.append(v)
    i += 1

j = 0
for value in word_value:
    if value in tri_values:
        j += 1
print(j)