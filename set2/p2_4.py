def largest_number(input_list: list):
    if(len(input_list) == 0 or len(input_list) == 1):
        return None

    max_number = input_list[0]

    for number in input_list:
        if(number > max_number):
            max_number = number

    return max_number


def second_largest_number(input_list: list):
    if(len(input_list) == 0 or len(input_list) == 1):
        return None

    input_list.remove(largest_number(input_list))
    return largest_number(input_list)

print(second_largest_number([-1,2,3,3564]))