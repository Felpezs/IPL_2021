dividend = 25
divisor = 30
quociente = 0 
resto = 0

if(dividend >= 0 and divisor > 0):
    while(True): 
        resto_aux = dividend - quociente * divisor
        
        if(resto_aux < 0):
            quociente -= 1
            break
        
        resto = resto_aux

        quociente += 1

out = (quociente, resto)