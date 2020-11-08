#Quadratic Programm

def quadratic(x1,x2):
    
    a = 1

    b = - (x1+x2)
    
    c = (x1*x2)
    
    return a,b,c

print(quadratic(2,6))