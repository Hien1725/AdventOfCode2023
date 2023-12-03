def get_position_symbols(s,y):
    positions = []
    list_of_char = list(enumerate(s))
    for (index, char) in list_of_char:
        #if char != '.' and not char.isdigit():
        if char in '*/=+%@#&-$':
            
            positions.append((index, y))

    return positions

def get_positions_around_a_number(x, y, length):
    positions = []
    y_left_upper_corner = y - 1
    y_right_low_corner = y + 1
    x_left_upper_corner = x - 1
    x_right_low_corner = x + length

    left_upper_corner = (x_left_upper_corner, y_left_upper_corner)
    right_low_corner = (x_right_low_corner, y_right_low_corner)
    
    #positions à gauche et à droite
    positions.append((x - 1, y))
    positions.append((x + length, y))

    #positions au-dessus et en-dessous
    for i in range(x_right_low_corner - x_left_upper_corner + 1):
        positions.append((x_left_upper_corner + i, y_left_upper_corner))
        positions.append((x_left_upper_corner + i, y_right_low_corner))

    return positions

def is_a_tuple_from_list1_in_list2_of_tuple(list1, list2):
    for tup in list1:
        if tup in list2:
            return True
    return False


path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 3\\input_test.txt"
path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 3\\input.txt"

positions_all_symbols = []
with open(path) as file:
    data = file.readlines()
    for (index, line) in enumerate(data):
        line = line.replace('\n','')
        positions_all_symbols += get_position_symbols(line, index)

count = 0
with open(path) as file:
    data = file.readlines()
    for (index, line) in enumerate(data):
        line = line.replace('*','.')
        line = line.replace('\n','')
        
        # Pas moyen de comprendre pourquoi les + et - font bugger le système. Je les enlève
        line = line.replace('+','.')
        line = line.replace('-','.')

        # D'autres font aussi bugger le système. J'enlève tout.
        for char in line:
            if char in '*/=+%@#&-$':
                line = line.replace(char,'.')

        list_number_in_line = [int(s) for s in line.split('.') if s.isdigit()]

        for num in list_number_in_line:
            string_number = str(num)
            i = line.find(str(string_number))
            length = len(string_number)

            if is_a_tuple_from_list1_in_list2_of_tuple(get_positions_around_a_number(i, index, length), positions_all_symbols) == True:
                count += num

            #day 2
        

print(count)
