def get_position_gears(s,y):
    """Extracts positions of symbols from a line."""
    positions = []
    list_of_char = list(enumerate(s))
    for (index, char) in list_of_char:
        if char == '*':
        #if char in '*/=+%@#&-$':
            
            positions.append((index, y))

    return positions

def get_positions_around_a_gear(x, y):
    """Calculates positions around a digit in a matrix."""
    return get_positions_around_a_number(x, y, 1)

def get_positions_around_a_number(x, y, length):
    """Calculates positions around a number in a matrix."""
    positions = []

    x_left_upper_corner = x - 1
    x_right_low_corner = x + length
    y_left_upper_corner = y - 1
    y_right_low_corner = y + 1
    
    #positions à gauche et à droite
    positions.append((x - 1, y))
    positions.append((x + length, y))

    #positions au-dessus et en-dessous
    for i in range(x_right_low_corner - x_left_upper_corner + 1):
        positions.append((x_left_upper_corner + i, y_left_upper_corner))
        positions.append((x_left_upper_corner + i, y_right_low_corner))

    return positions

def is_a_tuple_from_list1_in_list2_of_tuple(list1, list2):
    """Checks if any tuple from list1 is in list2."""
    for tup in list1:
        if tup in list2:
            return True
    return False

def get_indexes_and_numbers(line):
    """Finds indexes and corresponding numbers in a line."""
    last_index = len(line) - 1

    number_positions = []

    whole_number = ''
    is_first = True
    for index, char in enumerate(line):
        if char.isdigit():
            if is_first == True:
                i = index
            whole_number += char
            is_first = False

            if index == last_index or not line[index + 1].isdigit():
                number_positions.append((i, int(whole_number)))

        else:
            is_first = True
            whole_number = ''

    return number_positions

path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 3\\input.txt"
# path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 3\\input_test.txt"

positions_all_gears = []
with open(path) as file:
    data = file.readlines()
    for (index, line) in enumerate(data):
        line = line.replace('\n', '')
        positions_all_gears += get_position_gears(line, index)

all_numbers_and_positions = []
count = 0
with open(path) as file:
    data = file.readlines()
    for (index, line) in enumerate(data):
        line = line.replace('*','.')
        line = line.replace('\n','')
        
        for char in line:
            if char in '+-*/=+%@#&-$':
                line = line.replace(char,'.')
        
        # attention, si plusieurs fois la même valeur dans une ligne, il ne faut pas compter encore et encore la première
        list_tuple_numbers_in_line = get_indexes_and_numbers(line)

        for i_num, num in list_tuple_numbers_in_line:
            string_number = str(num)
            length = len(string_number)

            if is_a_tuple_from_list1_in_list2_of_tuple(get_positions_around_a_number(i_num, index, length), positions_all_gears):
                count += num

            pos = []
            for a in range(length):
                pos.append((i_num + a, index))
            tup_num = (num, pos)
            all_numbers_and_positions.append(tup_num)


list_gears = []

for (x, y) in positions_all_gears:
    list_gear = []

    for (num, list) in all_numbers_and_positions:
        if is_a_tuple_from_list1_in_list2_of_tuple(get_positions_around_a_gear(x, y), list):
            list_gear.append(num)

    if not list_gear == []:
        list_gears.append(list_gear)

count = 0
for list in list_gears:
    if len(list) == 2:
        count += list[0] * list[1]

print(count)