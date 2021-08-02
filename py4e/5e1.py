# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

count = 0
total = 0
while True:
    get_num = input("Enter a number: ")
    if get_num == "done" : break
    try :
        num = int(get_num)
    except :
        print("Invalid input")
        continue
    count = count + 1
    total = total + num
    if count is None or total is None:
        count = 1
        total = num

print('Sum:', total)
print('Entries:', count)
print('Average:', total / count)
