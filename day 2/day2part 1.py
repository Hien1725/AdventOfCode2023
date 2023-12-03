# str_test = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'

# test = str_test.split(":")
# game = test[0]
# results = test[1].split(";")
# test = results
# print(results)

def give_tuple_rgb(s):
    r = 0
    g = 0
    b = 0
    list = s.split(",")

    for elem in list:
        if 'red' in elem:
            r = get_number(elem)
        elif 'green' in elem:
            g = get_number(elem)
        elif 'blue' in elem:
            b = get_number(elem)

    return (r, g, b)

def give_list_tuples_rgb(list):
    list_tuples = []
    for elem in list:
        list_tuples.append(give_tuple_rgb(elem))
    
    return list_tuples

def get_number(s):
    temp = ''
    for e in s:
        if e in '0123456789':
            temp += e
    return int(temp)

def was_possible(real_tuple,given_tuple):
    g_r, g_g, g_b = given_tuple
    r_r, r_g, r_b = real_tuple

    if g_r > r_r or g_g > r_g or g_b > r_b:
        return False
    
    return True

def complex_was_possible(real_tuple,list_given_tuple):
    for elem in list_given_tuple:
        if not was_possible(real_tuple,elem):
            return False
        
    return True

# print(give_list_tuples_rgb(results))

# real_tuple = (0, 1 , 2)
# given_tuple = (0, 1 , 2)
# list_given_tuple = [(0,0,0), given_tuple]

# print(complex_was_possible(real_tuple,list_given_tuple))

given_red = 12
given_green = 13
given_blue = 14
real_tuple = (given_red, given_green, given_blue)

count = 0

with open("C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 2\\input.txt") as file:
    data = file.readlines()
    for line in data:
        cut = line.split(":")
        list_given_results = cut[1].split(";")
        list_given_tuple = give_list_tuples_rgb(list_given_results)
        if complex_was_possible(real_tuple,list_given_tuple):
            game = get_number(cut[0])
            count += game

print(count)
