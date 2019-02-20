'''
# (DAY 1)
# Find all numbers divisable by 7 but not a multiple of 5
empty_list = []

for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        empty_list.append(str(i))

print(','.join(empty_list))

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

# (DAY 3)
# Integral number n, create a dictionary 
print('Enter in a number: ')
n = int(input())
d = dict()
for i in range(1, n+1):
    d[i] = i*i
print(d)

'''

# (DAY 4)

values = input('Give me some comma seperated numbers:')
list = values.split(',')
tuple = tuple(list)
print(list, tuple)