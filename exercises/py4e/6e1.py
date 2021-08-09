# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

spaceship = 'galactica'
print(len(spaceship))
print("Starting:")
i = -1
while i >= 0-len(spaceship):
    letter = spaceship[i]
    print(letter)
    i = i - 1
