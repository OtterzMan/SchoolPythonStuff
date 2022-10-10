def Grader(grade):
    if grade >= 80:
        print("9")
        
    if grade >= 67 and grade < 80:
        print("8")
        
    if grade >= 54 and grade < 67:
        print("7")
        
    if grade >= 41 and grade < 54:
        print("6")
        
    if grade >= 31 and grade < 41:
        print("5")
        
    if grade >= 22 and grade < 31:
        print("4")
        
    if grade >= 13 and grade < 22:
        print("3")
        
    if grade >= 4 and grade < 13:
        print("2")
        
    if grade >= 2 and grade < 4:
        print("1")
        
    if grade < 2:
        print("U")
        
Grader(67)