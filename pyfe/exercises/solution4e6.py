def computepay(hours, rate) :
    if hours > 40 :
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else :
        pay = rate * hours
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
hours = float(sh)
rate = float(sr)

xp = computepay(hours,rate)

print("Pay:", xp)
