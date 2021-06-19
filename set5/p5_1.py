def run_langton(rules, size):
    
    ant_pos_x, ant_pos_y = ((size // 2), (size // 2))
    ant_orientation = [1, 0, 0, 0]
    grid = []

    count = 0
    for rows in range(size):
        aux_list = []
        for cols in range(size):
            aux_list.append(0)
    
        grid.append(aux_list)

    while(0 <= ant_pos_x < size and 0 <= ant_pos_y < size):
        count += 1
        grid[ant_pos_x][ant_pos_y] = (grid[ant_pos_x][ant_pos_y] + 1) % len(rules)
        last_orientation = ant_orientation.index(1)

        if last_orientation == 0:
            ant_pos_x -= 1
        elif last_orientation == 1:
            ant_pos_y += 1
        elif last_orientation == 2:
            ant_pos_x += 1
        elif last_orientation == 3:
            ant_pos_y -= 1 

        if(not(0 <= ant_pos_x < size) or not(0 <= ant_pos_y < size)):
            break
        grid_value = grid[ant_pos_x][ant_pos_y]
        rotate = rules[grid_value % len(rules)]

        if rotate.lower() == 'r':
            ant_orientation[last_orientation] = 0
            ant_orientation[(last_orientation + 1) % 4] = 1

        else:
            ant_orientation[last_orientation] = 0
            ant_orientation[(last_orientation - 1) % 4] = 1

        #grid[ant_pos_x][ant_pos_y] = (grid[ant_pos_x][ant_pos_y] + 1) % len(rules)

    return (count, grid)