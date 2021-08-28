# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidencevalues from these lines. When you reach the end of the file, print out the average spam confidence.


sample = input("File to parse: ")
handle = open(sample)


count = 0
sum = 0
value = 0

def find_dspam():
    for line in handle:
        found = line.find('X-DSPAM-Confidence:')
        grab = line[found+1:]
        # num = grab.lstrip()
        # Python trims white space during float conversion
        value  = float(grab)

def find_totals():
    for value in handle:
        count = count + 1
        sum = sum + value
            


