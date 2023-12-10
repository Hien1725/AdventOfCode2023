import time
import re
from math import lcm

def list_of_keys_ending_with(dictionary, char):
    return [key for key in dictionary if key[-1] == char]

def main():
    """
    Solve the Day 8 Part 2 challenge of Advent of Code 2023.

    This program reads a list of left/right instructions and a network of labeled nodes.
    It starts on every node that ends with 'A' and follows the instructions simultaneously,
    seeking a loop that ends with nodes ending in 'Z'. Once the loop is found for each starting
    node, the program calculates the number of steps it takes for all nodes to end in 'Z' at the same time.

    Returns:
        None
    """

    # Part 2
    start_time_part2 = time.time()

    path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 8\\input.txt"
    # path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 8\\input_test_part2.txt"
    
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

    current_list_keys = list_of_keys_ending_with(dict_of_tuples, 'A')
    
    list_of_infos = [] # récupérons les informations (Tuple à l'origine de la loop, Début de la loop, Fin de la loop, index de Z)
    for key in current_list_keys:
        current_key = key
        list_of_tuples = []
        solution_found = False
        index_of_Z = 0 # Only one was found

        while not solution_found:
            for i in range(len(directions_int)):
                current_tuple = (current_key, i)

                if current_tuple in list_of_tuples:
                    list_of_tuples.append(current_tuple)
                    solution_found = True
                    break
                else:
                    list_of_tuples.append(current_tuple)
                
                inst = directions_int[i]
                current_key = dict_of_tuples[current_key][inst]

                if current_key[-1] == 'Z':
                    index_of_Z = len(list_of_tuples)

        print('Dernier tuple = ' + str(list_of_tuples[-1]))
        print('Première instance de ' + str(list_of_tuples[-1]) + ' trouvée = ' + str(list_of_tuples.index(list_of_tuples[-1])))
        print('Dernière instance de ' + str(list_of_tuples[-1]) + ' trouvée = ' + str(len(list_of_tuples) - 1))
        print('Z se trouve en ' + str(index_of_Z) + '\n')

        list_of_infos.append((list_of_tuples[-1], list_of_tuples.index(list_of_tuples[-1]), len(list_of_tuples) - 1, index_of_Z))

    end_time_part2 = time.time()
    execution_duration_part2 = end_time_part2 - start_time_part2
    steps = 0
    print("Part 2:", steps)
    print(f"Part 2 took {execution_duration_part2} seconds to run.")

    # Laziness to create a function that calculates all cases when, in this case, there is only one Z for each A
    print(lcm(15871, 21251, 16409, 11567, 18023, 14257))

if __name__ == "__main__":
    main()
