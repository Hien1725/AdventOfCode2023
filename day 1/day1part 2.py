def return_first(s):
    """Returns the first digit found in the string."""
    for char in s:
        if char in '123456789':
            return char
        
def invert_string(s):
    """Inverts the characters in the string."""
    reversed_string = ''
    for char in s:
        reversed_string = char + reversed_string 
    return reversed_string 

def return_last(s):
    """Returns the last digit found in the inverted string."""
    inverted = invert_string(s)
    return return_first(inverted)

def convert_str_num(s):
    """Converts words representing numbers to their corresponding digits."""
    num_dict = {'one': 'o1ne', 'two': 't2wo', 'three': 't3hree', 'four': 'f4our', 'five' : 'f5ive', 'six' : 's6ix', 'seven' : 's7even', 'eight' : 'e8ight', 'nine' : 'n9ine'}

    for word in num_dict:
        s = s.replace(word, num_dict[word])

    return s

def calibration_value(s):
    """Calculates the calibration value by combining the first and last digits."""
    first_digit = return_first(s)
    last_digit = return_last(s)
    return int(first_digit + last_digit)

count = 0
with open("C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 1\\input.txt") as file:
    data = file.readlines()
    for line in data:
        converted_line = convert_str_num(line)
        count += calibration_value(converted_line)

print(count)
