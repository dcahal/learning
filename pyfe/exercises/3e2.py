# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. 

hrs = input("Enter Hours: ")

try: 
    hr = float(hrs)
except :
    print("Error: Please try again using numeric input.")
    exit()

bpays = input("Enter Hourly Pay: ")

try:
    bpay = float(bpays)
    # opay = bpay * 1.5
except :
    print("Error: Please try again using numeric input.")
    exit()

if 0 < hr <= 40 :
    print(hr * bpay)
elif hr > 40 :
    print(40 * bpay + (hr - 40) * bpay * 1.5)
else :
    print('Invalid work hours!')
