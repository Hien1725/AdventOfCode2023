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

def hash_algo(input_string, hash_value = 0):
    """
    Run the HASH algorithm on the given input string.

    Args:
        input_string (str): The input string to hash.
        hash_value (int, optional): The current value of the hash algorithm. Defaults to 0.

    Returns:
        int: The result of running the HASH algorithm on the input string.
    """
    for char in input_string:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256
    return hash_value

def main():
    """
    Solve the Day 15 puzzle "Lens Library".

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
    start_time_part1 = time.time()
    result1 = 0

    data = read_data(path)
    initialization_sequence = data[0].split(',')

    for step in initialization_sequence:
        result1 += hash_algo(step, 0)

    end_time_part1 = time.time()
    execution_duration_part1 = end_time_part1 - start_time_part1

    print("Part 1:", result1)
    print(f"Part 1 took {execution_duration_part1} seconds to run.")

if __name__ == "__main__":
    main()