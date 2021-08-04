# Find largest number
largest = None
print('Before', largest)
for num in [9, 41, 12, 3, 74, 15] :
    if largest is None :
        largest = num
    elif num > largest :
        largest = num
    print(largest, num)
print('After', largest)

# Find average
count = 0
sum = 0
print('Before', count, sum)
for num in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + num
    print(count, sum, num)
print('After', sum / count)

# Variable can be declared in For statement and assigned to iterate in given sequence
