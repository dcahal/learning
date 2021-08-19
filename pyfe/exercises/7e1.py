mbox = open('mbox-short.txt')
num = 0
for line in mbox:
    print(line.upper())
    num = num + 1
