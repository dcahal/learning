# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

cstr = input("Enter a temperature in degrees Celsius: ")
c = float(cstr)
f = 32 + c * 1.8
print("Temperature in Fahrenheit:", f)
