import time
import os

def read_data(path):
    """
    Read data from a file specified by the given path.

    Args:
        path (str): The path to the input file.

    Returns:
        list: A list containing lines read from the file.
    """
    with open(path) as file:
        data = file.readlines()
    return data

def set_working_directory():
    """
    Set the working directory to the script's directory and return the folder path.

    Returns:
        str: The absolute path to the current working directory.
    """
    # Retrieve the script's path
    script_path = os.path.abspath(__file__)
    # Retrieve the script's directory
    script_directory = os.path.dirname(script_path)
    # Change the current working directory to the script's directory
    os.chdir(script_directory)
    # Now, os.getcwd() should return the correct path
    folder_path = os.getcwd()
    return folder_path


    """
    Find the index of the line of reflection in a pattern across a vertical line.

    Args:
        pattern (list): List of strings representing a pattern.

    Returns:
        int: The index of the line of reflection.
    """
    return find_horizontal_mirror(transpose_a_pattern(pattern))

def transpose_table(data):
    """
    Transpose a pattern represented by a list of strings.

    Args:
        pattern (list): List of strings representing a pattern.

    Returns:
        list: List of strings representing the transposed pattern.
    """
    lines = [list(line.rstrip()) for line in data]

    rslt = []
    for i in range(len(lines[0])):
        temp = []
        for j in range(len(lines)):
            temp.append(lines[j][i])
        rslt.append(''.join(temp))
    return rslt       

def find_indices_of_character(s,sub):
    return [index for index, char in enumerate(s) if char == sub]

def rearrange_line_by_rock_direction(line, bol):
    """
    rearrange_line_by_rock_direction a line by moving rounded rocks according to the specified direction.

    Args:
        line (str): The input line.
        bol (bool): True for north direction, TBD for others.

    Returns:
        str: The rearrange_line_by_rock_directiond line.
    """
    indexes = find_indices_of_character(line, '#')
    rslt = []
    line_listed = line.split('#')
    for s in line_listed:
        sorted_str = sorted(s, reverse=bol)
        rslt += sorted_str
    
    for index in indexes:
        rslt.insert(index, '#')

    return ''.join(rslt)

def give_value(s):
    """
    Calculate the total load caused by rounded rocks in a line.

    Args:
        s (str): The input line.

    Returns:
        int: The total load caused by rounded rocks in the line.
    """
    rslt = 0
    length = len(s)
    indexes = find_indices_of_character(s,'O')
    for index in indexes:
        rslt += length - index

    return rslt

def tilt_table_in_direction(data, dir = 'north'):
    """
    Tilt the table in the specified direction.

    Args:
        data (list): List of strings representing the input data.
        direction (str): The direction to tilt the table, 'north' for now.

    Returns:
        list: List of strings representing the tilted table.
    """
    rslt = []
    bol = True
    if dir == 'north' or 'south':
        data = transpose_table(data)
    
    if dir == 'south' or 'east':
        bol = True

    for line in data:
        line = rearrange_line_by_rock_direction(line, bol)
        rslt.append(line)
    return rslt

def main():
    """
    Solve the Day 14 puzzle "Parabolic Reflector Dish".

    Args:
        None

    Returns:
        None
    """

    # Define the path to the input file
    folder_path = set_working_directory()
    input_name = "input.txt"
    input_name = "input_test.txt"
    path = folder_path + "\\" + input_name
       
    # Part 1
    start_time_part1 = time.time()
    result1 = 0

    data = read_data(path)
    data = tilt_table_in_direction(data)

    for line in data:
        result1 += give_value(line)

    end_time_part1 = time.time()
    execution_duration_part1 = end_time_part1 - start_time_part1

    print("Part 1:", result1)
    print(f"Part 1 took {execution_duration_part1} seconds to run.")

    # Part 2
    start_time_part2 = time.time()
    result2 = 0
    number_of_cycles = 1000000000
    number_of_turns = int(number_of_cycles / 4)
    data = read_data(path)

    for i in range(number_of_turns):
        print(i)
        data = tilt_table_in_direction(data, 'north')
        data = tilt_table_in_direction(data, 'west')
        data = tilt_table_in_direction(data, 'south')
        data = tilt_table_in_direction(data, 'east')

    for line in data:
        result1 += give_value(line)

    end_time_part2 = time.time()
    execution_duration_part2 = end_time_part2 - start_time_part2
    print("Part 2:", result2)
    print(f"Part 2 took {execution_duration_part2} seconds to run.")

if __name__ == "__main__":
    main()