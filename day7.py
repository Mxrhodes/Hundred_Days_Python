'''

Day 1

_list = []

for i in range(2000, 3201):
    if i % 7 === 0 and i % 5 != 0:
        _list.append(str(i))
    print(','.join(_list))

Day 2 

def factorial(num):
    if num < 0:
        return "Must be greater than 0"
    if num == 0:
        return 1
    return num * factorial(num-1)
print('Enter an integer... ')
num = int(input())
print(factorilal(num))

Day 3

print("Enter a number: ")

n = int(input())
d = dict()
for i in range=(1, n +1):
    d[i] = i*i
print(d)

Day 4

values = input('Enter comma sepeerated numbers: ')
list = values.split(',')
tuple = tuple(list)
print(list,tuple)

Day 5

Class Mama(object):

    def __init__(self):
        self.s = ''
    def getString(self):
        self.s = input('Enter a String... ')
    def printstring(self):
        print(self.s.upper())

Day 6

import math
c = 50
h = 30

x = [] #location for all the answers
y = [i for input('Enter a number or numbers: ').split(',')] # contains users entered number(s)
for d in y:
    x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(x))

'''

#Day 7
# Take 2 digits, x and y as inputs and generate a 2-D array.

input_for_system = input("Type input here: ")
dimension = [int(x) for x in input_for_system.split(',')]

rowin = dimension[0]
colin = dimension[1]
list = [[0 for column in range(colin)] for rows in range(rowin)]

for row in range(rowin):
    for col in range(colin):
        list[row][col] = row*col
print(list)

