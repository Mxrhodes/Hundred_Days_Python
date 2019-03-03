'''


Day 11

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

'''

#Day 12

#Accept a string and calculate number of letters and digits
sen = input("Enter a sentance")
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