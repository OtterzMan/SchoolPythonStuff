month = input("Choose a number between 1-12:")

month = int(month)

if month == 1:
    MonthText = "January"
    
if month == 2:
    MonthText = "February"
    
if month == 3:
    MonthText = "March"

if month == 4:
    MonthText = "April"
    
if month == 5:
    MonthText = "May"
    
if month == 6:
    MonthText = "June"
    
if month == 7:
    MonthText = "July"
    
if month == 8:
    MonthText = "August"
    
if month == 9:
    MonthText = "September"
    
if month == 10:
    MonthText = "October"
    
if month == 11:
    MonthText = "November"

if month == 12:
    MonthText = "December"
    

def ValidMonth():
    if month > 0 and month < 13:
        print("Valid month !!!","  The Month You Selected is:", MonthText)
        
    else:
        print("Invalid Month")
        
ValidMonth()