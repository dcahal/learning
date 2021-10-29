#!/bin/python3

for num in range(1,250) :
    if num == 1 :
        continue
    for i in range(2,250) :
        divisors = 0
        if  num <= i :
            break
        elif num % i == 0 :
            divisors = divisors + 1
            break
        else :
            continue
    if divisors == 0 :
        print(num)
