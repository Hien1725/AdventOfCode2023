import time
import re

def is_all_elem_ending_with_char(l, char):
    for elem in l:
        if elem[-1] != char:
            return False
    return True

def main():
    """
    Solve the Day 8 Part 1 challenge of Advent of Code 2023.

    This program reads a list of left/right instructions and a network of labeled nodes.
    It navigates the network based on the instructions, starting from node AAA, and counts
    the steps required to reach the node ZZZ.

    Returns:
        None
    """
    
    # Define the path to the input file
    path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 8\\input.txt"
    # path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 8\\input_test.txt"

    # Part 1
    start_time_part1 = time.time()

    dict_of_tuples = {}
    with open(path) as file:
        data = file.readlines()
        directions = list(data[0].strip())
        directions_str = data[0].strip()
        directions_int = directions_str.replace('R', '1').replace('L', '0')
        directions_int = [1 if direction == 'R' else 0 for direction in directions]
        
        for line in data[2:]:
            temp = re.findall(r'\b\w+\b', line)
            dict_of_tuples[temp[0]] = (temp[1], temp[2])
        
    current_key = 'AAA'
    searched_key = 'ZZZ'

    steps = 0
    searched_key_found = False
    while True:
        for inst in directions_int:
            if current_key == searched_key:
                searched_key_found = True
                break

            current_key = dict_of_tuples[current_key][inst]
            steps += 1
            
        if searched_key_found:
            break
        
    end_time_part1 = time.time()
    execution_duration_part1 = end_time_part1 - start_time_part1

    print("Part 1:", steps)
    print(f"Part 1 took {execution_duration_part1} seconds to run.")

if __name__ == "__main__":
    main()
