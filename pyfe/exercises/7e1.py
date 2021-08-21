# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:

mbox = open('../provided/mbox-short.txt')
num = 0
for line in mbox:
    line = line.upper()
    print(line.rstrip())
    num = num + 1
