import time

def is_key_in_map(k, line):
    # destination_range_start = int(line[0])
    source_range_start = int(line[1])
    range_length = int(line[2])
    return k >= source_range_start and k < source_range_start + range_length

def get_key_value_in_map(k, map):
    for line in map:
        if is_key_in_map(k, line):
            destination_range_start = line[0]
            source_range_start = line[1]
            # range_length = line[2]
            delta = k - source_range_start
            return destination_range_start + delta
        
    return k

def get_parameters_from_line(line):
    temp = line.split()
    destination_range_start = int(temp[0])
    source_range_start = int(temp[1])
    range_length = int(temp[2])
    return [destination_range_start, source_range_start, range_length]

path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 5\\input.txt"
# path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 5\\input_test.txt"

start_time = time.time()

indexes_converter = []
data = []

with open(path) as file:
    data = file.readlines()
    for i in range(len(data)):
        if '-' in data[i]:
            indexes_converter.append(i)

seeds = data[0].split()[1:]
soils = []
fertilizers = []
waters = []
lights = []
temperatures = []
humiditys = []
locations = []

seed_to_soil_map = []
for i in range(indexes_converter[0] + 1, indexes_converter[1] - 1):
    seed_to_soil_map.append(get_parameters_from_line(data[i]))

soil_to_fertilizer_map = []
for i in range(indexes_converter[1] + 1, indexes_converter[2] - 1):
    soil_to_fertilizer_map.append(get_parameters_from_line(data[i]))

fertilizer_to_water_map = []
for i in range(indexes_converter[2] + 1, indexes_converter[3] - 1):
    fertilizer_to_water_map.append(get_parameters_from_line(data[i]))

water_to_light_map = []
for i in range(indexes_converter[3] + 1, indexes_converter[4] - 1):
    water_to_light_map.append(get_parameters_from_line(data[i]))

light_to_temperature_map = []
for i in range(indexes_converter[4] + 1, indexes_converter[5] - 1):
    light_to_temperature_map.append(get_parameters_from_line(data[i]))

temperature_to_humidity_map = []
for i in range(indexes_converter[5] + 1, indexes_converter[6] - 1):
    temperature_to_humidity_map.append(get_parameters_from_line(data[i]))
   
humidity_to_location_map = []
for i in range(indexes_converter[6] + 1, len(data)):
    humidity_to_location_map.append(get_parameters_from_line(data[i]))

locations = []
for i in range(len(seeds)):
    soils.append(get_key_value_in_map(int(seeds[i]), seed_to_soil_map))
    fertilizers.append(get_key_value_in_map(int(soils[i]), soil_to_fertilizer_map))
    waters.append(get_key_value_in_map(int(fertilizers[i]), fertilizer_to_water_map))
    lights.append(get_key_value_in_map(int(waters[i]), water_to_light_map))
    temperatures.append(get_key_value_in_map(int(lights[i]), light_to_temperature_map))
    humiditys.append(get_key_value_in_map(int(temperatures[i]), temperature_to_humidity_map))
    locations.append(get_key_value_in_map(int(humiditys[i]), humidity_to_location_map))

    # print(locations[i])

print(soils)
print(fertilizers)
print(waters)
print(lights)
print(temperatures)
print(humiditys)
locations = sorted(locations)
print(locations[0])

end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds.")