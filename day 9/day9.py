import time
import os
import re

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

def is_all_zeros(sequence):
    """
    Check if all values in a sequence are zero.

    Args:
        sequence (list): The sequence of values.

    Returns:
        bool: True if all values are zero, False otherwise.
    """
    # return all(value == 0 for value in sequence) is better
    for i in sequence:
        if i != 0:
            return False
    return True

def create_all_sequences(history, is_in_the_future):
    """
    Create sequences of differences until the sequence is entirely zero.

    Args:
        history (list): The input sequence.
        is_in_the_future (bool): True for forward extrapolation, False for backward extrapolation.

    Returns:
        list: List of sequences representing differences.
    """
    sequences = [history]
    print(sequences)
    if not is_in_the_future:
        sequences.reverse()
        print(sequences)
    current_sequence = []
    
    while not is_all_zeros(sequences[-1]):
        current_sequence = sequences[-1]
        temp_sequence = []
        
        for i in range(1, len(current_sequence)):
            temp_sequence.append(current_sequence[i]-current_sequence[i-1])
        
        sequences.append(temp_sequence)

    return sequences

def next_value_prediction(history, is_in_the_future = True):
    """
    Extrapolate the next value for a given history.

    Args:
        history (list): The input sequence.
        is_in_the_future (bool): True for forward extrapolation, False for backward extrapolation.

    Returns:
        int: The extrapolated next value.
    """
    result = 0
    sequences = create_all_sequences(history, is_in_the_future)

    for sequence in sequences:
        result += sequence[-1]
    
    return result

def main():
    """
    Read input data, perform forward and backward extrapolation, and print results.
    """
    # Define the path to the input file
    folder_path = set_working_directory()
    input_name = "input.txt"
    input_name = "input_test.txt"

    path = folder_path + "\\" + input_name
    print(path)
    
    # Part 1
    result1 = 0
    start_time_part1 = time.time()

    list_of_all_entry_sequences = []
    data = read_data(path)
    for line in data:
        # line = re.findall(r'\b\w+\b', line)
        line = line.split()

        temp_int_seq = []
        for s in line:
            temp_int_seq.append(int(s))
        
        list_of_all_entry_sequences.append(temp_int_seq)

    for sequence in list_of_all_entry_sequences:
        result1 += next_value_prediction(sequence)

    end_time_part1 = time.time()
    execution_duration_part1 = end_time_part1 - start_time_part1

    print("Part 1:", result1)
    print(f"Part 1 took {execution_duration_part1} seconds to run.")

    # Part 2
    result2 = 0
    for sequence in list_of_all_entry_sequences:
        
        result2 += next_value_prediction(sequence, False)

    print("Part 2:", result2)

if __name__ == "__main__":
    main()
