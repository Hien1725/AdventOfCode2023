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

def transpose_the_data(data):
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

def find_all(s,sub):
    return [index for index, char in enumerate(s) if char == sub]

def rearrange(line):
    indexes = find_all(line, '#')
    rslt = []
    line_listed = line.split('#')
    for s in line_listed:
        sorted_str = sorted(s, reverse=True)
        rslt += sorted_str
    
    for index in indexes:
        rslt.insert(index, '#')

    return ''.join(rslt)

def give_value(s):
    rslt = 0
    length = len(s)
    indexes = find_all(s,'O')
    for index in indexes:
        rslt += length - index

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
    result1 = 0
    start_time_part1 = time.time()

    data = read_data(path)
    data = transpose_the_data(data)

    for line in data:
        print(rearrange(line))
        result1 += give_value(rearrange(line))
        

    end_time_part1 = time.time()
    execution_duration_part1 = end_time_part1 - start_time_part1

    print("Part 1:", result1)
    print(f"Part 1 took {execution_duration_part1} seconds to run.")

    # Part 2
    # result2 = 0
    # print("Part 2:", result2)

if __name__ == "__main__":
    main()