#Welche Quarter of Month

def quarter_of(month):
    
    zahl = int(month)
    
    if 1 <= zahl <= 3:
    
        return print(1)
    
    elif 4 <= zahl <= 6:
        
        return print(2)
        
    elif 7 <= zahl <= 9:
    
        return print(3)
    
    elif 10 <= zahl <= 12:
        
        return print(4)
    else:
        
        return print("Bitte schreiben Sie gültige Zahl - (1 bis 12) ")

quarter_of(5)