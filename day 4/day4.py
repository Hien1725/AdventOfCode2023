path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 4\\input.txt"

line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
winning_numbers, elf_numbers = line.split('|')
winning_numbers = winning_numbers.split()
winning_numbers = winning_numbers[2:]

elf_numbers = elf_numbers.split()

def give_lists(s):
    winning_numbers, elf_numbers = s.split('|')
    winning_numbers = winning_numbers.split()
    winning_numbers = winning_numbers[2:]
    elf_numbers = elf_numbers.split()
    return winning_numbers, elf_numbers

def points_value(winning_numbers, elf_numbers):
    winning_points = 0
    for val in elf_numbers:
        if val in winning_numbers:
            winning_points +=1
    if winning_points == 0:
        return 0
    else:
        return 2 ** (winning_points - 1)
    
def count_matching_numbers(winning_numbers, elf_numbers):
    winning_points = 0
    
    for val in elf_numbers:
        if val in winning_numbers:
            winning_points +=1
    
    return winning_points


#part 1
count = 0
with open(path) as file:
    data = file.readlines()
    for line in data:
        winning_numbers, elf_numbers = give_lists(line)
        count += points_value(winning_numbers, elf_numbers)

print(count)

#part 2
count_line = 0
matching_numbers_of_cards = []

with open(path) as file:
    data = file.readlines()
    for line in data:
        count_line += 1
        winning_numbers, elf_numbers = give_lists(line)
        matching_numbers_of_cards.append(count_matching_numbers(winning_numbers, elf_numbers))

number_of_scratchcards = [1] * count_line

for i in range(count_line):
    for j in range(matching_numbers_of_cards[i]):
        number_of_scratchcards[i + j + 1] += number_of_scratchcards[i]

count_of_scratchcards = 0
for scratchcards in number_of_scratchcards:
    count_of_scratchcards += scratchcards

print(count_of_scratchcards)