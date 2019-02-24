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

Day 3

print("Enter a number: ")
n = int(input())
d = dict()

for i in range(1, n+1):
    d[i] = i *i
print(d)

Day 4

values = input("Enter comma seperated values: ")
list = values.split(',')
tuple = tuple(list)
print(list, tuple)

Day 5 

Class Mom(object):
    def __init__(self):
        self.n = ''

    def getName(self):
        self.n = str(input("Enter name for Mom: "))
    
    def printMomsName(self):
        print(self.n.upper())

Day 6

import math

c = 50
h = 30

x = []
y = [i for input("Enter a number or numbers: ").split(',')]
for d in y:
    x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(x))

Day 7

input_for_system = input("Enter input: ")
dimension = [int(x) for x in input_for_system.split(',')]
rowin = dimension[0]
colin = dimension[1]

list = [[0 for column in range(colin)] for rows in range(rowin)]
for row in range(rowin):
    for col in range(colin):
        list[row][col] = row*col
print(list)

'''
#Day 8

# to get each item in list printed I could...
pets = ['dog', 'cat', 'bird', 'rabbit', 'fish', 'neighbor']

print(pets[0])
print(pets[1])
print(pets[2])
print(pets[3])
print(pets[4])
print(pets[5], '/n')

#or use a for loop to print everything in pets

for doodeledy in pets:
    print(doodeledy)

#rock out a conditional statement with a while loop

i_got_20_bucks = 20

while i_got_20_bucks < 35:
    print(i_got_20_bucks)
    i_got_20_bucks += 1
print("I need more money")

# for all numbers between 1500 and 2700, which are divisible by 7 and a multiple of 5

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

#write a program that will guess a number between 1 and 10

import random

target_num, guess_num = random.randint(1,10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10, and keep guessing till correct'))
print('game over')

#create a cool printed pattern that looks like a sideways triangle

count = 0
for num in range(7):
    count += 1
    print('*' * count)
for num in range(6):
    count -= 1
    print('*' * count)