'''

Day 1 

_list = []

for i in range(2000, 3201):
    if (i % 7 === 0) and (i % 5 != 0):
        _list.append(str(i))

Day 2

def factorial(num):
    if num < 0:
        return "Must be greater than zero"
    if num == 0:
        return 1
    return num * factorial(num -1)

Day 3

n = int(input())
d = dict()

for i in range(1, n+1):
    d[i] = i * i
print d

Day 4

values = input("Enter cs numbers")
list = values.split(',')
tuple = tuple(list)

Day 5 

class example(object):
    def __init__(self):
        self.a = ''
    def getString(self):
        self.a = input("Enter a String")
    def printString(self):
        print(self.a.lower())
'''
# Day 6 
# Cool calculator using formula Q = square root of [(2*c*d)/h]

import math
x = []
y = [i for i in input("Give me a number: ").split(',')]
for d in y:
    x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(x))