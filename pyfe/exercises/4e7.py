# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

sscore = input("Enter Score: ")
fscore = float(sscore)

def computegrade(score) :
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

grade = computegrade(fscore)
print(grade)

