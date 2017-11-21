'''
Using names.txt, a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical 
value for each name, multiply this value by its alphabetical position in the 
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
'''
def get_letter_num(letter):
    return ord(letter)-64

def get_name_sum(name):
    return sum(map(get_letter_num,list(name)))

name = 'COLIN'

with open('pro_22.txt','r') as f:
    line = f.read()

name_list = list(map(eval,line.split(',')))
name_list.sort()
s = 0
for i,name in enumerate(name_list):
    s += (i+1)*get_name_sum(name)
print(s)