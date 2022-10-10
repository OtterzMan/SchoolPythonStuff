def Nitrate(NitrateLvl):
    if NitrateLvl > 10:
        print("Dose 3")
        
    if NitrateLvl < 10 and NitrateLvl > 2.5:
        print("Dose 2")
        
    if NitrateLvl < 2.5 and NitrateLvl > 1:
        print("Dose 1")
        
    if NitrateLvl < 1:
        print("Dose 0.5")
        
Nitrate(6)