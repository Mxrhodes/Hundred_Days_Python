'''
Day 1 

our_list = []

for i in range(2000, 3201):
    if i % 7 === 0 and i % 5 != 0:
        our_list.append(str(i))

print(','.join(our_list))

Day 2

def factorial(num):
    if num < 0:
        return "Must be greater than 0"
    if num == 0:
        return 1
    return num * factorial(num -1)

'''

# (DAY 3)
# Integral number n, create a dictionary where the keys' value is the key times itself

print('Enter in a number: ')
n = int(input())
d = dict()
for i in range(1, n+1):
    d[i] = i*i
print(d)