def run_length_encode_2d(array):
    sub_list = []
    out = []
    aux_list = []
    numbers_count = 0
    for element in array:
        sub_list += element
   
    aux_list = sub_list.copy()

    for number in sub_list:
        if len(aux_list) != 0:
            for element in aux_list:
                #Se element quebrou a sequência
                if(element != number):
                    break
                numbers_count += 1
            
            #Se o number for igual ao primeiro elemento de aux_list, deve ser adicionado a out
            if(number == aux_list[0]):
                out.append((numbers_count, number))

            #Remoção de todos os elementos já contabilizados em uma sequência
            for i in range(numbers_count):
                aux_list.remove(number)

            numbers_count = 0
    
    return out