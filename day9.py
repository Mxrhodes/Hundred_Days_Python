'''

Day 1

_list = []

for i in range(2000, 3201):
    if i%7 == 0 and i%5 != 0:
        _list.append(str(i))
    print(','.join(_list))

Day 2

def factorial(num):
    if num < 0:
        return "Must be greater than zero"
    if num == 0:
        return 1
    return num * factorial(num-1)

Day 3

print("Enter a number: ")
n = int(input())
d = dict()

for i in range(i, n+1):
    d[i] = i * i
print(d)

Day 4

values = input("Enter comma seperated: ")
list = values.split(',')
tuple = list(tuple)
print(list,tuple)

Day 5 

Class Mama(object):
    def __init__(self):
        self.s = ''
    def getInput(self):
        self.s = input("Enter a string: ")
    def printGetInput(self):
        print(self.s.upper())

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

Day 8

pets = ['dog', 'cat', 'bitd', 'rabbit', 'fish', 'neighbor']

print(pets[0])

for i in pets:
    print(i)

got20 = 20

while got20 < 35:
    print(got20)
    got20 += 1
print("I need more money")

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

import random

target_num, guess_num = random.randint(1,10), 0
while target_num != guess_num:
    guess_num = int(input("Take a guess from 1 - 10: "))
print("Game over")

count = 0
for num in range(7):
    count += 1
    print('*' * count)
for num in range(6):
    count -= 1
    print('*' * count)

'''

# Day 9

#create an array of 5 integers and display array items, access them via index
from array import *
array_num = array('i', [1,3,5,7,9])
for i in array_num:
    print(i)

#append a new item to end of an array
print("starting array ", array_num)
array_num.append(11)
print('New array: ', array_num)

#reverse the order
print(array_num[::-1]) #Start at the beginning and end at the end (::)
print('Change ', array_num[::-3])
#insert a new value before the number 3
print(array_num)
array_num.insert(1,4)
print("CORRECTION : ", array_num)

#remove an item via index
array_num.pop(3) # removes index
print(array_num)

#remove the first occurance of an element
new_array = array('i', [1,3,5,7,3,9,3,11])
print(new_array)
new_array.remove(3) # removes specified item

#covert an array into a list
print(type(new_array))
x = new_array.tolist()
print(type(x))