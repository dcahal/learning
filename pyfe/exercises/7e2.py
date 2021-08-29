# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidencevalues from these lines. When you reach the end of the file, print out the average spam confidence.


sample = input("File to parse: ")
opened = open(sample)

count = 0
total = 0

for line in opened:
    # May use line.startswith() for this problem. This solution supports inline matches
    found = line.find('X-DSPAM-Confidence:')
    if found == -1 :
        continue
    else :
        count = count + 1
        # Found match at rune #, grab text after 19 character pattern
        grab = line[found+19:].strip()
        value  = float(grab)
        total = total + value
        mean = total / count

print("Matching lines:" , count)    
print("Average confidence value:" , mean)
