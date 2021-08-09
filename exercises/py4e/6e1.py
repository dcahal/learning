# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

spaceship = 'galactica'
ifirst = 0 - len(spaceship)
print(ifirst)

# Index 0 starts second iteration of string. Start with index -1, the last letter.
print("Starting:")
i = -1
while i >= ifirst:
    letter = spaceship[i]
    print(letter)
    i = i - 1
