# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidencevalues from these lines. When you reach the end of the file, print out the average spam confidence.


# sample = input("File to parse: ")
# handle = open(sample)


count = 0
total = 0
value = 0

handle = open("../provided/mbox-short.txt")


def find_totals(opened) :
    for value in opened:
        count = count + 1
        total = total + value
        mean = total / count


def find_dspam(opened) :
    count = 0
    total = 0
    for line in opened:
        found = line.find('X-DSPAM-Confidence:')
        if found == -1 :
            continue
        grab = line[found+19:]
        num = grab.strip()
        value  = float(num)
        count = count + 1
        total = total + value
        mean = total / count
        print(count)

find_dspam(handle)

#mean = total / count
#print("Matching lines: " , count)    
print("Average confidence value: " , mean)
