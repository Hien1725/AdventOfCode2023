import time

def read_data(path):
    with open(path) as file:
        data = file.readlines()
    return data

def main():
    # Define the path to the input file
    path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 9\\input.txt"
    path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 9\\input_test.txt"
    
    # Part 1
    result = 0
    start_time_part1 = time.time()

    with open(path) as file:
        data = file.readlines()
        pass
        
    end_time_part1 = time.time()
    execution_duration_part1 = end_time_part1 - start_time_part1

    print("Part 1:", result)
    print(f"Part 1 took {execution_duration_part1} seconds to run.")

if __name__ == "__main__":
    main()
