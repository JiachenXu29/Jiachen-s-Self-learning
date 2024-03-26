score = int (input("score: "))

# comparing grade
def grade1():
    if score >= 90 and score <= 100:
        print("Grade: A")
    elif score >= 80 and score < 90:
        print("Grade: B")   
    elif score >= 70 and score < 80:
        print("Grade: C")   
    elif score >= 60 and score < 70:
        print("Grade: D")   
    else:
        print("Grade: F")   

# comparing grade by ptyhon's trick
def grade2():
    if 90 <= score <= 100:
        print("Grade: A")
    elif 80 <= score < 90:
        print("Grade: B")   
    elif 70 <= score < 80:
        print("Grade: C")   
    elif 60 <= score < 70:
        print("Grade: D")   
    else:
        print("Grade: F") 

# return grade
def grade3(none):
    if 90 <= score <= 100:
        return("Grade: A")
    elif 80 <= score < 90:
        return("Grade: B")   
    elif 70 <= score < 80:
        return("Grade: C")   
    elif 60 <= score < 70:
        return("Grade: D")   
    else:
        return("Grade: F") 

# better simplized version
def grade4():
    if 90 <= score:
        return("Grade: A")
    elif 80 <= score:
        return("Grade: B")   
    elif 70 <= score :
        return("Grade: C")   
    elif 60 <= score:
        return("Grade: D")   
    else:
        return("Grade: F") 


print(f"your final grade is {grade4()}")