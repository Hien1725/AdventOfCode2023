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

def dist_btw_galaxies(t1, t2, values_lines, values_columns):
    x1, y1 = t1
    x2, y2 = t2
    dist = 0
    for i in range(min(x1, x2), max(x1, x2)):
        dist += values_lines[str(i)]

    for i in range(min(y1, y2), max(y1, y2)):
        dist += values_columns[str(i)]

    return dist

def main():
    """
    Read input data, perform forward and backward extrapolation, and print results.
    """
    # Define the path to the input file
    folder_path = set_working_directory()
    input_name = "input.txt"
    # input_name = "input_test.txt"

    path = folder_path + "\\" + input_name
       
    # Part 1 and 2
    result = 0
    start_time_part1 = time.time()

    data = read_data(path)

    expension_value = 1000000

    indexes_of_galaxies = []
    values_of_lines = {}
    values_of_columns = {}
    galaxy_matrix  = []
    for index_line, line in enumerate(data):
        line = line.split()
        
        temp_galaxy_matrix  = []
        is_line_empty = True
        for index_char, char in enumerate(line[0]):

            temp_galaxy_matrix.append(char)
            
            if char == '#':
                indexes_of_galaxies.append((index_line, index_char))
                is_line_empty = False
            
            if is_line_empty :
                values_of_lines[str(index_line)] = expension_value
            else:
                values_of_lines[str(index_line)] = 1

        galaxy_matrix .append(temp_galaxy_matrix)

    
    for index_column in range(len(line[0])):
        is_column_empty = True
        for index_line in range(len(data)):
            if galaxy_matrix [index_line][index_column] == '#':
                is_column_empty = False
        if is_column_empty:
            values_of_columns[str(index_column)] = expension_value
        else :
            values_of_columns[str(index_column)] = 1
    
    # print(values_of_lines)
    # print(values_of_columns)
            
    # print(indexes_of_galaxies)

    for i in range(len(indexes_of_galaxies)):
        for j in range(i + 1, len(indexes_of_galaxies)):
                # print('dist entre ' + str(indexes_of_galaxies[i]) + ' et ' + str(indexes_of_galaxies[j]) + ' est : ' + str(dist_btw_galaxies(indexes_of_galaxies[i], indexes_of_galaxies[j], values_of_lines, values_of_columns)))
                result += dist_btw_galaxies(indexes_of_galaxies[i], indexes_of_galaxies[j], values_of_lines, values_of_columns)

    end_time_part1 = time.time()
    # execution_duration_part1 = end_time_part1 - start_time_part1

    print("Part 1:", result)
    # print(f"Part 1 took {execution_duration_part1} seconds to run.")

    # Part 2
    # result2 = 0
    # print("Part 2:", result2)

if __name__ == "__main__":
    main()