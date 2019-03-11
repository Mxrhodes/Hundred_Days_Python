'''
print("day 1")

_list = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        _list.append(str(i))
    print(",".join(_list))

print("Day 2")

def factorial(num):
    if num = 0:
        return 1
    return num *(factorial(num -1))
print(factorial(5))

Print("Day 3")

print("Enter a number: ")
n = int(input())
d = dict()

for i in range(1, n+1):
    d[i] = i*i
print("d: :, d)

print("Day 4")

values = input("Enter comma seperated values: ")
list = values.split(',')
tuple = tuple(list)
print(list, tuple)

pirnt("Day 5")

class Mama(object):
    def __init__(self):
        self.s = ''
    def getString(self):
        self.s = input()
    def printGetString(self):
        print(self.s)

m = Mama()
m.getString()
m.printGetString()

print("Day 6")

import math

c = 50
h = 30

x = []
y = [i for i in input("Enter a number or set of numbers: ").split(',')] 
for d in y:
    x.append(str(int(round(math.sqrt(2*c*float(d)/h))))
print(','.join(x))

print("Day 7")

input_system = input("Enter input for x and y")
dimension = [int(x) for x in input_system.split(',')]
rowin = dimension[0]
colin = dimension[1]
list = [[0 for column in range(colin)]for rows in range(rowin)]
for rows in range(rowin):
    for col in range(colin):
        list[row][col] = row*col
print(list)

Print("Day 8")

pets = ['dog', 'cat', 'bird', 'rabbit', 'fish', 'neighbor']

for i in pets:
    print(i)

got20 = 20

while got20 < 35:
    print(got20)
    got20 += 1
print("Need some mo")

print("Day 9")

from array import *

array_num = array('i', [1,3,5,7,9])
for i in array_num:
    print(i)

array_num.append(11)
print(array_num[::-1])

print(array_num.insert(1,4))
array_num.pop(3)
array_num.remove(5)

print("Day 10")

x = input("Type a word: ")
b = ''.join(reversed(x))
print(b)
print("or")
print(x[::-1])

def oddEvenCount(x):
    odd_count = 0
    even_count = 0
    for i in x:
        if i % 2 == 0:
            even_count +=1
        else:
            odd_count +=1
    return" Odd count: " + str(odd_count) + " Even count: " + str(even_count)

x = range(1,12)
print(oddEVenCount(x))

data = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {'class':'V', 'Section':'A'}]

for index in data:
    print("Type of ", index, "is ", type(index))

for i in range(1,8):
    if i != 3 and i != 6:
        print(i)

#fibonacci
def fibonacci(num):
    x,y = 0,1
    while y < num:
        x,y = y, x+y
        print("\n")

for ice in range(1, 50):
    if ice % 3 == 0:
        print('SUPAA')
    elif ice % 5 == 0:
        print('BADASS')
    elif ice % 3 == 0 and ice % 5 == 0:
        print('super badass')
    else:
        print(str(ice) + " is not")

print("Day 11")

row_num = int(input("How many rows: "))
col_num = int(input("How many columns: "))

list = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        list[row][col] = row*col
print(list, '\n')

lines = []
while True:
    l = input("Enter a phrase: ")
    if l:
        lines.append(l.upper())
    else:
        break
for l in lines:
    print(l)

def dividableBinary():
    seq = input("Enter a sequence of c.s 4 didgit binary nums")
    seq = seq.split(',)
    for s in seq:
        if int(str(s),2) % 5 == 0:
            print("Output: ", s)
dividableBinary()

print("Day 12")

#Accept a string and calculate number of letters and digits
sen = input("Enter a sentance: ")
num, lett = 0, 0
for s in sen:
    if s.isalpha():
        lett += 1
    elif s.isdigit():
        num +=1
    else:
        pass
print("Letters: ", lett)
print("Numbers: ", num)

#Check the validity of a password

import re # used for matching
passw = input("Enter password: ")
x = True

while x:
    if(len(passw) < 6 or len(passw) > 16):
        break
    elif not re.search('[a-z]', passw):
        break
    elif not re.search('[0-9]', passw):
        break
    elif not re.search('[A-Z]', passw):
        break
    elif not re.search('[$@$_]', passw):
        break
    elif re.search('\s', passw): # '\s' matches the whitespaces
        break
    else:
        print("Password check complete. Your password was accepted!")
        x = False
        break
if x:
    print("That is a BS password - you are banned for life")

#Find numbers between 100 and 400 both included, where each digit is even
# print in csv sequence

even_digits = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        even_digits.append(s)
print(",".join(even_digits))

#Create a program that will print out a pattern of an 'A'
letter_A = ''
for row in range(8):
    for column in range(8):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            letter_A = letter_A + '*'
        else:
            letter_A = letter_A + ' '
    letter_A = letter_A + '\n'
print(letter_A)

'''
print("Day 13")
#Make a grid and find out how to move the dots to the right to make it on s
#lets do the smae for "s"

letter_s = ''
for row in range(7):
    for col in range(7):
        if ((row == 0 or row == 3 or row == 6) and col>0 and col <7):
            letter_s += '*'
        elif ((row == 1 or row == 2) and col ==1):
            letter_s += '*'
        elif ((row == 4 or row == 5) and col == 6):
            letter_s += '*'
        else:
            letter_s += ' '      
    letter_s += '\n'
print(letter_s)

x = ''
for row in range(7):
    for col in range(7):
        if (((col == 1 or col == 5) and (row > 4 or row < 2)) or row == col and col > 0 and col < 6 or (col -- 2 and row == 4) or (col == 4 and row == 2)):
            x += '*'
        else:
            x += ' '      
    x += '\n'
print(x) # find the error

#python program which calculates age in dog years
# dog year 0-2 = 10.5 human years each year
# after that each dog year = 4 human years
human = int(input("How many human years has the dog been alive? "))
if human < 0:
    print("Age must be a positive number")
    exit()
elif human <= 2:
    dog_age = human * 10.5
else:
    dog_age = (human - 2) * 4 + 21
print("The dog's age in dog years is: ", dog_age)

# python program to check if letter is a vowel or a consonant

x = input("Chose any letter from the alphabet: ")
if x in ('a','e','i','o','u'):
    print('{} is a vowel'.format(x))
elif x == 'y':
    print("A, E, I, O, U and sometimes Y")
else:
    print(f'{x} is a constonant')

# give me a month and i'll share the number of days

abr_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
print(f'List of months: {abr_months}')

month = input('Enter an abreviated month: ')
if month not in abr_months:
    month = input("Try entering the month again: ")
elif month == 'Feb':
    print('Number of days: 28/29 days')
elif month in ('Apr', 'Jun', 'Sept', 'Nov'):
    print("Number of days: 30 days") 
elif month in ('Jan', 'Mar', 'May', 'July', 'Aug', 'Oct', 'Dec'):
    print("Number of days: 31 days") 
else:
    print(f'What did you just type in {month}')