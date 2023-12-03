count = 0
with open("C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 3\\input.txt") as file:
    data = file.readlines()
    for (index, line) in enumerate(data):
        line = line.replace('*','.')
        line = line.replace('\n','')
        print((index,line))