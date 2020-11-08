
#Securty Entippen und Ausgeben

def maskify(cc):
    
    i = len(cc)
    
    x_ebene = []
    
    if i <=4:
        return print("".join(cc))
        
    else:
        for line in range(0,i-4):
            x_ebene.append("#")
        
        x_ebene.append(cc[i-4])
        x_ebene.append(cc[i-3])
        x_ebene.append(cc[i-2])
        x_ebene.append(cc[i-1])
        
        
        
        if cc != "".join(x_ebene):
            print()
            
        return print("".join(x_ebene))
    #print(",".join(x_ebene))

maskify("098790878798798")