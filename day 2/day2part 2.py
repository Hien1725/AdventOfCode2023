def extract_rgb_values(s):
    """Extracts red, green, and blue values from a string."""
    red, green, blue = 0, 0, 0
    input_list = s.split(",")

    for elem in input_list:
        if 'red' in elem:
            red = extract_number(elem)
        elif 'green' in elem:
            green = extract_number(elem)
        elif 'blue' in elem:
            blue = extract_number(elem)

    return (red, green, blue)

def give_list_tuples_rgb(input_list):
    """Converts a list of strings into a list of RGB tuples."""
    #solution chatGPT : list_tuples = [extract_rgb_values(elem) for elem in input_list]
    list_tuples = []
    for elem in input_list:
        list_tuples.append(extract_rgb_values(elem))
    
    return list_tuples

def extract_number(s):
    """Extracts numerical values from a string."""
    #solution chatGPT : return int(''.join(char for char in s if char.isdigit()))
    temp = ''
    for char in s:
        if char in '0123456789':
            temp += char
    return int(temp)

def is_possible(real_tuple,given_tuple):
    """Checks if given RGB values are possible given real RGB values."""
    g_r, g_g, g_b = given_tuple
    r_r, r_g, r_b = real_tuple

    if g_r > r_r or g_g > r_g or g_b > r_b:
        return False
    
    return True

def all_games_possible(real_tuple,list_given_tuple):
    """Checks if all given RGB values in a list are possible given real RGB values."""
    #solution chatGPT : return all(is_possible(real_rgb, given_rgb) for given_rgb in list_given_rgb)
    for elem in list_given_tuple:
        if not is_possible(real_tuple,elem):
            return False
        
    return True

def find_minimum_set(list_of_tuples):
    """Finds the minimum set of RGB values from a list of tuples."""
    red, green, blue = list_of_tuples[0]
    for r, g, b in list_of_tuples:
        red = max(red, r)
        green = max(green, g)
        blue = max(blue, b)

    return (red, green, blue)

def calculate_tuple_power(tup):
    """Calculates the power of an RGB tuple."""
    red, green, blue = tup
    return red * green * blue

given_red = 12
given_green = 13
given_blue = 14
real_tuple = (given_red, given_green, given_blue)

count_possible_games = 0
total_power = 0

with open("C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 2\\input.txt") as file:
    data = file.readlines()
    for line in data:
        cut = line.split(":")
        list_given_results = cut[1].split(";")
        list_given_tuple = give_list_tuples_rgb(list_given_results)
        #day 1
        if all_games_possible(real_tuple,list_given_tuple):
            game_number = extract_number(cut[0])
            count_possible_games += game_number

        #day 2
        total_power += calculate_tuple_power(find_minimum_set(list_given_tuple))

print(count_possible_games)
print(total_power)

# tuples_list = [(4, 0, 3), (1, 2, 6), (0, 2, 8)]
# print(find_minimum_set(tuples_list))