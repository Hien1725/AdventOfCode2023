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

def next_pipe(char, x, y):
    # En entrant dans une pipe d'un côté, on ressort de l'autre
    if char == 'F':
        if x == 0:
            return (1,0)
        else:
            return (0,1)
    elif char == '|':
        if x == 1:
            return (-1,0)
        else:
            return (1,0)
    elif char == '-':
        if y == 1:
            return (0,-1)
        else:
            return (0,1)
    elif char == 'J':
        if x == -1:
            return (0,-1)
        else:
            return (-1,0)
    elif char == 'L':
        if y == 1:
            return (-1,0)
        else:
            return (0,1)
    elif char == '7':
        if x == 1:
            return (0,-1)
        else:
            return (1,0)

def give_two_dir(char):
    directions = []
    if char in 'F-L':
        directions.append((1,0))
    if char in 'F|J7':
        directions.append((0,1))
    if char in '|JL':
        directions.append((-1,0))
    if char in '-J7':
        directions.append((0,-1))
    return directions

def begin_loop(matrix, char, x, y):
    directions = give_two_dir(char)
    direction_1 = directions[0]
    direction_2 = directions[1]
    dx1, dy1 = direction_1
    dx2, dy2 = direction_2
    (x1, y1, char1) , (x2, y2, char2) = (matrix[x + dx1][y + dy1], matrix[x + dx2][y + dy2])


def loop_searcher(x, y, char):
    # en partant d'un point, vérifier les deux suivants, puis les deux suivants etc
    # arrêter la boucle
    #### si la pipe suivant ne présente pas d'entrée commune avec la sortie du précédent (. compris)
    #### renvoyer la longueur parcourue sur les deux points vérifiés sont au même endroit (signifie qu'on est au point le plus éloigné)
    pass

def main():
    """
    Read input data, perform forward and backward extrapolation, and print results.
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
    data_pipes = []
    dict_data_pipes = {}
    matrix_data_pipes = []
    for index_line, line in enumerate(data):
        line = line.split()
        
        temp_data_pipe = []
        temp_matrix_data_pipe = []
        for index_char, char in enumerate(line[0]):

            temp_data_pipe.append((index_line, index_char, char))
            temp_matrix_data_pipe.append(char)
            dict_data_pipes['(' + str(index_line) + ',' + str(index_char) + ')'] = char
            
        data_pipes.append(temp_data_pipe)
        matrix_data_pipes.append(temp_matrix_data_pipe)
    
    print(data_pipes)
    print(dict_data_pipes)
    print(matrix_data_pipes)

    loop_found = False
    test_while = 0
    
    for i in range(len(matrix_data_pipes[0])):
        for j in range(len(matrix_data_pipes[0])):
            for is_loop, length in loop_searcher(i,j):
                if is_loop:
                    print(length)
                    break
                

            
            
            while loop_found == False and test_while < 0:
        
        test_while += 1
    end_time_part1 = time.time()
    execution_duration_part1 = end_time_part1 - start_time_part1

    print("Part 1:", result1)
    print(f"Part 1 took {execution_duration_part1} seconds to run.")

    # Part 2
    result2 = 0
    

    print("Part 2:", result2)

if __name__ == "__main__":
    main()