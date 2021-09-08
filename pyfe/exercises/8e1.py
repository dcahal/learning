# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

items = ['a', 'b', 'c', 'd']

def chop(ls) :
    ls.pop(0)
    ls.pop(-1)

def middle(ls) :
    del ls[0]
    del ls[-1]

print(chop(items))
print(middle(items))
print(items)
