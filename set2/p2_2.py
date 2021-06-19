def prime(num):
    if(num == 0 or num == 1):
        return False

    if(num >= 3):
        if(num % 2 == 0):
            return False
    
        for i in range(3, num, 2):
            if(num % i == 0):
                return False  
    return True
