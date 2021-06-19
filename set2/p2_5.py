import string

lower_strings = string.ascii_lowercase
numbers = string.digits

def count_numbers(shift: int, limit: int):
    if(shift >= limit):
        while(shift >= limit):
            shift-=limit

    elif(shift < -limit):
        while(shift < -limit):
            shift += limit
            
    return shift

def caesar_cipher(text: str, shift: int):
    new_string = ''
    char_limit = 26
    number_limit = 10
    text = text.lower()

    shift_numbers = count_numbers(shift, number_limit)
    shift = count_numbers(shift, char_limit)

    for char in text:
        if(char.isdigit()):
            search_char = shift_numbers + numbers.find(char)
            new_string += numbers[count_numbers(search_char, number_limit)]

        elif(lower_strings.find(char) >= 0):
            search_char = shift + lower_strings.find(char)
            new_string += lower_strings[count_numbers(search_char, char_limit)]
        
        else:
            new_string += char

    return new_string