# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table: If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85. 

sscore = input("Enter Score: ")
score = float(sscore)

if 1 >= score >= 0.9 :
    print("A")
elif 0.9 > score >= 0.8 :
    print("B")
elif 0.8 > score >= 0.7 :
    print("C")
elif 0.7 > score >= 0.6 :
    print("D")
elif 0 <= score < 0.6 :
    print("F")
else :
    print("Invalid score. Score must be between 0 and 1.")
