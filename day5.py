'''

Day 1

_list = []

for i in range(2000, 3201):
    if i % 7 === 0 and i % 5 != 0:
        _list.append(str(i))

Day 2

def factorial(num):
    if num < 0:
        return "Must be greater than 0"
    if num == 0:
        return 1
    return num * factorial(num -1)

Day 3

n = int(input())
d = dict()
for i in range(i, n+i):
    d[i] = i * i
print d

Day 4

values = input("Enter some cs numbers")
list = values.split(',')
tuple = tuple(list)
print(list,tuple)
'''

# Day 5
# create a class with 2 methods

class Mama(object):
    def __init__(self):
        self.s = ''
    def getString(self):
        self.s = input('Give me a String...')
    def printString(self):
        print(self.s.upper())

x = Mama()
print(x)

x.getString()
x.printString()




