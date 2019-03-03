'''
Day 1

_list = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        _list.append(str(i))
    print(','.join(_list))

Day 2

def factorial(num):
    if num < 0:
        return "Must be greater than zeros"
    if num == 0:
        return 1
    return num * factorial(num - 1)

Day 3

print("Enter a number")
n = int(input())
d = dict()

for i in range(i, n+1):
    d[i] = i * i
print(d)

day 4

values = input("Enter comma seperated values")
list = values.split(',')
tuple = tuple(list)
print(list, tuple)

Day 5

Class Mama(object):

    def __init__(self):
        self.s = ''
    def getString(self):
        self.s = input("Enter a string: ")
    def printGetString(self):
        print(self.s.upper())

Day 6

import math

c = 50
h = 30

x = []
y = [i for input("Enter a number or numbers").split(',')]
for d in y:
    x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(x))

Day 7

input_system = input("Enter input: ")
dimension = [int(x) for x in input_system.split(',')]
rowin = dimension[0]
colin = dimension[1]

list = [[0 for column in range(colin)] for rows in range(rowin)]
for row in range(rowin):
    for col in range(colin):
        list[row][col] = row *col
print(list)

Day 8

pets = ['dog', 'cat', 'bird', 'rabbit', 'fish', 'neighbor']
print(pets[0])

for i in pets:
    print(i)

got20 = 20

while got20 < 35:
    print(got20)
    got20 += 1
print("Need more money now!")

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

import random
 
target_num, guess_num = random.randint(1,10), 0
while target_num != guess_num:
    guess_num = int(input("Take a guess from 1 - 10: "))
print("Game over")

count = 0 
for i in range(7):
    count+= 1
    print('*', count)
for i in range(6):
    count -= 1
    print('*', count)

Day 9

from array import * 

array_num = array('i', [1,3,5,7,9])
for i in array_num:
    print(i)

print("starting array ", array_num)
array_num.append(13)
print("New array: ", array_num)

print(array_num[::-1])

print(array_num)
array_num.insert(3,8)
print("Correction: ", array_num)

array_num.pop(3)
print(array_num)

new_array = array('i', [1,3,5,7,3,9,3,11])
new_array.remove(3)
print("New array: ", new_array)

print(type(new_array))
x = new_array.tolist()
print(type(x))

#Day 10

#reverse an input str

x = input('Type what you want to be reversed... ')
b = ''.join(reversed(x))
print(b)
print("--OPTION 2--")
# or, use a start end step. slices str steps of -1
print(x[::-1])

#count even or odd from a series of sumbers
def oddEvenCount(x):
    odd_count = 0
    even_count = 0
    for i in x:
        if i % 2 == 0:
            even_count +=1
        else:
            odd_count +=1
    return "Odd count: " + str(odd_count) + " Even count: " + str(even_count)

x = [1,2,3,4,5,6,7,8,9,10,11]
print(oddEvenCount(x))

#given the below list, print out the item and its type

data = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {'class':'V', 'Section':'A'}]

for index in data:
    print("Type of ", index, "is ", type(index))

#write program prints all numbers except 3 and 6
for i in range(1,7):
    if i != 3 and i != 6:
        print(i)

#program a fibonacci seq between 0 and 50. next number is found by adding 2 numbers before it
x,y = 0,1
while y < 50:
    print(y)
    x,y = y, x+y
print('n')

#write a program iterating 0 t0 50. If num is multiple of 3 print SUPAA.
#if num is multiple of 5 print BADASS. if num multiple of both print super badass.

for ice in range(1, 50):
    if ice % 3 == 0:
        print('SUPAA')
    elif ice % 5 == 0:
        print('BADASS')
    elif ice % 3 == 0 and ice % 5 == 0:
        print('super badass')
    else:
        print(str(ice) + " is not")

'''

#Day 11

#takes 2 digits (m and n, row and col respectively) as inputs and generates a 2darray.
#The element value in the i-th row and j-th column of the array should be i+j

row_num = int(input("How many rows: "))
col_num = int(input("How many columns: "))

list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        list[row][col] = row*col
print(list, '\n')

#Write a Python program that accepts a swquence of lower case lines(blank line to terminate)
# as inputs and prints the lines as outputs in upper case
lines = []
while True:
    l = input("Enter a phrase: ")
    if l:
        lines.append(l.upper())
    else:
        break
for l in lines:
    print(l)

#Write a program which accepts a seq of commas seperated 4 digit binary nums as input
# and print the numbers that are divisible by 5 in a cs seq.

def dividable_binary():
    seq = input('Enter the binaries: ')
    seq = seq.split(',')
    for s in seq:
        if int(str(s),2) % 5 == 0:
            print("Output: ", s)
dividable_binary()