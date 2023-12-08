def win_the_race(race_time, record_distance):
    count_of_possibilities = 0

    starting_speed = 0  # mm/s
    gain_per_second_of_pressing = 1  # mm/s
    winner_found = False

    for secs_pressing in range(0, race_time + 1):

        secs_travelling = race_time - secs_pressing
        speed = starting_speed + secs_pressing * gain_per_second_of_pressing
        distance = speed * secs_travelling

        if distance > record_distance:
            count_of_possibilities += 1
            winner_found = True

        elif distance <= record_distance and winner_found:
            return count_of_possibilities

    return count_of_possibilities

def main():
    import time

    path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 6\\input.txt"
    path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 6\\input_test.txt"

    #part 1
    with open(path) as file:
        data = file.readlines()
        line = [l.strip('\n\r') for l in data]
        line = [l.split() for l in line]
        line = [l[1:] for l in line]

    tuples = list(zip(line[0], line[1]))

    multiplication_result = 1
    for tup in tuples:
        race_time, record_distance = tup
        print(win_the_race(int(race_time), int(record_distance)))
        multiplication_result *= win_the_race(int(race_time), int(record_distance))

    print("Part 1:", multiplication_result)

    # Part 2
    start_time_part2 = time.time()
    single_race_tuple = (45988373, 295173412781210)
    single_race_time, single_race_record = single_race_tuple
    part2_result = win_the_race(int(single_race_time), int(single_race_record))
    print("Part 2:", part2_result)
    end_time_part2 = time.time()

    execution_duration_part2 = end_time_part2 - start_time_part2
    print(f"Part 2 took {execution_duration_part2} seconds to run.")

if __name__ == '__main__':
    main()
