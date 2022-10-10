def StateCheck(number):
    if number >= 100.0:
        print("Gasous")
    if 1.0 < number < 99.0:
        print("Liquid")
    if 1.0 > number:
        print("Solid")
        
StateCheck(45.75)