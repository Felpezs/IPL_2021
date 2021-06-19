def square(number:int):
    return number**2

def fourth_power(number:int):
    num_fourth_pow = square(number)
    return square(num_fourth_pow)

def perfect_square(number:int):
    if(number >= 0):
        sqr = int(number**(1/2))
        return number == sqr ** 2