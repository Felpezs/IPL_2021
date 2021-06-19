def ndoors(doors):
    door_change = []
    for i in range(doors):
        door_change.append(False)

    for iteration in range(doors):
        for door in range(doors):
            if((door + 1) % (iteration + 1) == 0):
                if(door_change[door] == True):
                    door_change[door] = False
                else:
                    door_change[door] = True
    
    return [index + 1 for index, door in enumerate(door_change) if door == True]