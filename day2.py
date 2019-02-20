'''
Day 1: Find all numbers divisable by 7 but not a multiple of 5 within range 2000 - 3200.

our_list = []

for i in range(2000, 3201):
    if i % 7 === 0 and i % 5 != 0:
        our_list.append(str(i))

print(','.join(our_list))
'''

# (DAY 2)
# Compute the factorial of a given number

def factorial(num):
    if num < 0:
        return "Must be greater than 0"
    if num == 0:
        return 1
    return num * factorial(num-1)

print('Enter an integer... ')
num = int(input())
print(factorial(num))