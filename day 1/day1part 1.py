s = "test1test2test"

def returnfirst(s):
    for l in s:
        if l in '1234567890':
            return l
        
def invertstring(s):
    temp = ''
    for l in s:
        temp = l + temp
    return temp

def returnlast(s):
    return returnfirst(invertstring(s))

def calibrationvalue(s):
    return int(returnfirst(s) + returnlast(s))

count = 0
with open("C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 1\\input.txt") as file:
    data = file.readlines()
    for line in data:
        count += calibrationvalue(line)

print(count)