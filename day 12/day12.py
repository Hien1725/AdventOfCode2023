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

def conditions_in_two_format(line):
    """
    Convert a line with condition records into a tuple with two elements.

    Args:
        line (str): A line containing condition records.

    Returns:
        tuple: A tuple with two elements - the condition string and a list of integers.
    """
    rslt = line.split()
    rslt[1] = [int(s) for s in rslt[1].split(',')]
    return rslt

def read_condition(s):
    """
    Read condition records and return a list of integers representing group sizes.

    Args:
        s (str): The condition string with '?' representing unknown springs.

    Returns:
        list: A list of integers representing the sizes of contiguous groups of broken springs.
    """
    rslt = []
    already_begun = False
    temp = 0
    for char in s:
        if char == '.' and already_begun:
            already_begun = False
            rslt.append(temp)
            temp = 0
        if char == '#':
            already_begun = True
            temp += 1
    if temp > 0:
        rslt.append(temp)

    return rslt

def give_indexes_of_unknowns(s):
    """
    Identify the indexes of '?' in a string.

    Args:
        s (str): The input string.

    Returns:
        list: A list of indexes where '?' occurs in the string.
    """
    return [i for i, char in enumerate(s) if char == '?']

def all_config_of_conditions(s):
    """
    Generate all possible configurations of a row with unknown springs represented by '?'.

    Args:
        s (str): The row string with '?' representing unknown springs.

    Returns:
        list: A list of all possible configurations.
    """
    indexes_of_unknowns = give_indexes_of_unknowns(s)
    
    all_configs = []
    
    temp = list(s)
    caracteres_possibles = ['.', '#']
    
    for index in range(2 ** len(indexes_of_unknowns)):
        binary_representation = bin(index)[2:].zfill(len(indexes_of_unknowns))
        
        for i, char in zip(indexes_of_unknowns, binary_representation):
            temp[i] = caracteres_possibles[int(char)]
            
        all_configs.append(''.join(temp))

    return all_configs

def main():
    """
    Solve the Day 12 puzzle "Hot Springs".

    Read input data, generate all possible configurations of operational and broken springs
    for each row, count the different arrangements that meet the given criteria, and
    print the sum of those counts.

    """
    # Define the path to the input file
    folder_path = set_working_directory()
    input_name = "input.txt"
    # input_name = "input_test.txt"
    path = folder_path + "\\" + input_name
       
    # Part 1
    result1 = 0
    start_time_part1 = time.time()

    data = read_data(path)
    for index, line in enumerate(data):
        print(index)
        s, li = conditions_in_two_format(line)
        all_config = all_config_of_conditions(s)
        for config in all_config:
            if read_condition(config) == li:
                result1 += 1
    
    end_time_part1 = time.time()
    execution_duration_part1 = end_time_part1 - start_time_part1

    print("Part 1:", result1)
    print(f"Part 1 took {execution_duration_part1} seconds to run.")

    # Part 2
    # result2 = 0
    # print("Part 2:", result2)

if __name__ == "__main__":
    main()