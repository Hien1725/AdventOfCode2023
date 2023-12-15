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

def find_pattern_indices(data):
    """
    Find the indices of patterns in the given data.

    Args:
        data (list): List of strings representing the input data.

    Returns:
        list: A list of tuples representing the start and end indices of patterns in the data.
    """
    indexes_of_patterns = []
    first = 0
    for index, line in enumerate(data):
        if line == '\n':
            last = index - 1
            indexes_of_patterns.append((first, last + 1))
            first = index + 1
    indexes_of_patterns.append((first, len(data)))

    return indexes_of_patterns

def find_horizontal_mirror(pattern):
    """
    Find the index of the line of reflection in a pattern across a horizontal line.

    Args:
        pattern (list): List of strings representing a pattern.

    Returns:
        int: The index of the line of reflection.
    """
    pattern = [line.rstrip() for line in pattern]
    previous_line = ''
    rslt = 0

    for index, line in enumerate(pattern):
        it_is_find = False

        if line == previous_line:
            it_is_find = True
            minimum = min(len(pattern) - index - 1, index - 1)

            if index > 1:
                for i in range(minimum):
                    if(pattern[index - 2 - i] != pattern[index + 1 + i]):
                        it_is_find = False
                
            if it_is_find:
                rslt = index
        
        previous_line = line

    return rslt

def find_vertical_mirror(pattern):
    """
    Find the index of the line of reflection in a pattern across a vertical line.

    Args:
        pattern (list): List of strings representing a pattern.

    Returns:
        int: The index of the line of reflection.
    """
    return find_horizontal_mirror(transpose_a_pattern(pattern))

def transpose_a_pattern(pattern):
    """
    Transpose a pattern represented by a list of strings.

    Args:
        pattern (list): List of strings representing a pattern.

    Returns:
        list: List of strings representing the transposed pattern.
    """
    lines = [list(line.rstrip()) for line in pattern]

    rslt = []
    for i in range(len(lines[0])):
        temp = []
        for j in range(len(lines)):
            temp.append(lines[j][i])
        rslt.append(''.join(temp))
    return rslt       

def main():
    """
    Solve the Day 13 puzzle "Point of Incidence".

    This function reads the input data from a file, processes it to find the patterns, 
    and calculates the sum of indices of reflections for both horizontal and vertical mirrors 
    in each pattern. The final result for Part 1 is printed along with the execution time.

    Args:
        None

    Returns:
        None
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
    indexes_of_patterns = find_pattern_indices(data)

    for t in indexes_of_patterns:
        start, last = t
        pattern = data[start:last]
        result1 += 100 * find_horizontal_mirror(pattern)
        result1 += find_vertical_mirror(pattern)

    end_time_part1 = time.time()
    execution_duration_part1 = end_time_part1 - start_time_part1

    print("Part 1:", result1)
    print(f"Part 1 took {execution_duration_part1} seconds to run.")

    # Part 2
    # result2 = 0
    # print("Part 2:", result2)

if __name__ == "__main__":
    main()