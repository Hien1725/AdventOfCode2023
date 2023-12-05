def create_dict(destination_range_start, source_range_start, range_length):
    dict = {}
    for i in range(range_length):
        dict = dict | {str(source_range_start + i): (destination_range_start + i)}
    return dict

def merge(dict1, dict2):
    res = dict1 | dict2
    return res

path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 5\\input.txt"
#path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 5\\input_test.txt"


indexes_converter = []
data = []

with open(path) as file:
    data = file.readlines()
    for i in range(len(data)):
        if '-' in data[i]:
            indexes_converter.append(i)

seeds = data[0].split()[1:]

dict_seed_to_soil = {}
for i in range(indexes_converter[0] + 1, indexes_converter[1] - 1):
    temp = data[i].split()
    destination_range_start = int(temp[0])
    source_range_start = int(temp[1])
    range_length = int(temp[2])
    dict_seed_to_soil = dict_seed_to_soil | create_dict(destination_range_start, source_range_start, range_length)

dict_soil_to_fertilizer = {}
for i in range(indexes_converter[1] + 1, indexes_converter[2] - 1):
    temp = data[i].split()
    destination_range_start = int(temp[0])
    source_range_start = int(temp[1])
    range_length = int(temp[2])
    dict_soil_to_fertilizer = dict_soil_to_fertilizer | create_dict(destination_range_start, source_range_start, range_length)

dict_fertilizer_to_water = {}
for i in range(indexes_converter[2] + 1, indexes_converter[3] - 1):
    temp = data[i].split()
    destination_range_start = int(temp[0])
    source_range_start = int(temp[1])
    range_length = int(temp[2])
    dict_fertilizer_to_water = dict_fertilizer_to_water | create_dict(destination_range_start, source_range_start, range_length)

dict_water_to_light = {}
for i in range(indexes_converter[3] + 1, indexes_converter[4] - 1):
    temp = data[i].split()
    destination_range_start = int(temp[0])
    source_range_start = int(temp[1])
    range_length = int(temp[2])
    dict_water_to_light = dict_water_to_light | create_dict(destination_range_start, source_range_start, range_length)

dict_light_to_temperature = {}
for i in range(indexes_converter[4] + 1, indexes_converter[5] - 1):
    temp = data[i].split()
    destination_range_start = int(temp[0])
    source_range_start = int(temp[1])
    range_length = int(temp[2])
    dict_light_to_temperature = dict_light_to_temperature | create_dict(destination_range_start, source_range_start, range_length)

dict_temperature_to_humidity = {}
for i in range(indexes_converter[5] + 1, indexes_converter[6] - 1):
    temp = data[i].split()
    destination_range_start = int(temp[0])
    source_range_start = int(temp[1])
    range_length = int(temp[2])
    dict_temperature_to_humidity = dict_temperature_to_humidity | create_dict(destination_range_start, source_range_start, range_length)

dict_humidity_to_location = {}
for i in range(indexes_converter[6] + 1, len(data)):
    temp = data[i].split()
    destination_range_start = int(temp[0])
    source_range_start = int(temp[1])
    range_length = int(temp[2])
    dict_humidity_to_location = dict_humidity_to_location | create_dict(destination_range_start, source_range_start, range_length)

locations = []
for seed in seeds:
    soil = dict_seed_to_soil.get(seed,seed)
    fertilizer = dict_soil_to_fertilizer.get(soil,soil)
    water = dict_fertilizer_to_water.get(fertilizer,fertilizer)
    print(water)
    light = dict_water_to_light.get(water,water)
    temperature = dict_light_to_temperature.get(light,light)
    humidity = dict_temperature_to_humidity.get(temperature,temperature)
    location = dict_humidity_to_location.get(humidity,humidity)
    locations.append(location)

locations = sorted(locations)
print(locations)

"""     for line in data:
        print(line)
        data.append(line)
    print(data) """

#['seed-to-soil','soil-to-fertilizer','fertilizer-to-water','water-to-light','light-to-temperature','temperature-to-humidity','humidity-to-location']