# (DAY 1)
# Find all numbers divisable by 7 but not a multiple of 5

empty_list = []

for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        empty_list.append(str(i))

print(','.join(empty_list))
