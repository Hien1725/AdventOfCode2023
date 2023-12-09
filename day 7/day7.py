import time

def hand_ranking(s):
    '''Evaluate the ranking of a poker hand represented by a string of 5 characters.
    
    Args:
        s (str): A string containing 5 characters, representing cards.
                Each character can be one of the following: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
    
    Returns:
        int: The ranking of the poker hand, with the following possible values:
             6 - Five of a kind - 1 occ de 5 - 1
             5 - Four of a kind - 1 occ de 4 - 1 et 1 de 1 - 2
             4 - Full house - 1 occ de 3 et 1 de 2 - 2
             3 - Three of a kind - 1 occ de 3 et 1 de 1 et 1 de 1 - 3
             2 - Two pairs - 2 occ de 2 et une de 1 - 3
             1 - One pair - 1 occ de 2 et 3 de 1 - 4
             0 - High card - 5 occ de 1 - 5
    '''
    
    occurences = {}
    for char in s:
        if char in occurences:
            occurences[char] += 1
        else:
            occurences[char] = 1

    diff_cards = len(occurences)
    if diff_cards == 1:
        return 6
    elif diff_cards == 2 and max(occurences.values()) == 4:
        return 5
    elif diff_cards == 2:
        return 4
    elif diff_cards == 3 and max(occurences.values()) == 3:
        return 3
    elif diff_cards == 3:
        return 2
    elif diff_cards == 4:
        return 1
    else:
        return 0

def change_one_char(s, ss, index):
    return s[:index] + ss + s[index + 1:]

def get_indexes_of_J(s):
    indexes_of_J = []
    for index, char in enumerate(s):
        if char == 'J':
            indexes_of_J.append(index)
    return indexes_of_J

def all_jokers_possibilities_helper(s, cards, current_combination, index, list_of_combinaisons):
    if index == len(current_combination):
        list_of_combinaisons.append(current_combination)
        return

    for card in cards:
        new_combination = change_one_char(current_combination, card, index)
        all_jokers_possibilities_helper(s, cards, new_combination, index + 1, list_of_combinaisons)

def all_jokers_possibilities(s):
    cards = 'AKQT98765432'
    list_of_possibles_hands = []
    indexes_of_J = get_indexes_of_J(s)
    s = s.replace('J', 'K')

    if indexes_of_J == []:
        return [s]

    for index, index_of_J in enumerate(indexes_of_J):
        for card in cards:
            current_combination = change_one_char(s, card, index_of_J)
            list_of_possibles_hands.append(current_combination)
            if index != (len(indexes_of_J) - 1):
                all_jokers_possibilities_helper(s, cards, current_combination, indexes_of_J[index + 1], list_of_possibles_hands)
    return list_of_possibles_hands

def give_global_list_of_hands_ranking(hands):
    best_ranking = hand_ranking(hands[0])
    
    for hand in hands:
        temp_hand_ranking = hand_ranking(hand)
        if temp_hand_ranking > best_ranking:
            best_ranking = temp_hand_ranking
    
    return best_ranking


def give_card_ranking(char, joker_value):
    '''Assign a numerical value to a playing card character.'''
    cards_values = {'A' : 14, 'K' : 13, 'Q' : 12, 'J' : joker_value, 'T' : 10, '9' : 9, '8' : 8, '7' : 7, '6' : 6, '5' : 5, '4' : 4, '3' : 3, '2' : 2}
    return cards_values.get(char)

def give_hand_ranking(s, joker_value):
    
    '''Assign a numeric value to the strength of a poker hand by prioritizing the first character, then the second, and so on.
'''
    rst = 0
    
    for i in range(0, len(s)):
        dec_i = len(s) - (i + 1)
        rst += give_card_ranking(s[i], joker_value) * (10 ** (2 * dec_i))

    return rst

def give_global_hand_ranking(s, joker_value):
    '''Assign the total strength value to a poker hand, taking into account both the suit and individual card values.'''

    return hand_ranking(s) * 10**10 + give_hand_ranking(s, joker_value)
  
def give_global_hand_ranking_with_jokers(s, joker_value):
    '''Assign the total strength value to a poker hand, taking into account both the suit and individual card values.'''
    list_of_possibilities = all_jokers_possibilities(s)
    best_ranking = give_global_list_of_hands_ranking(list_of_possibilities)

    return best_ranking * 10**10 + give_hand_ranking(s, joker_value)

def main():

    path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 7\\input.txt"
    # path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 7\\input_test_test.txt"

    # Part 1
    start_time_part1 = time.time()
    joker_value = 11

    result = 0
    strengths = []
    dictionnary_strenght_bets = {}
    with open(path) as file:
        data = file.readlines()
        for line in data:
            line = line.split()
            strength = give_global_hand_ranking(line[0], joker_value)
            strengths.append(strength)
            dictionnary_strenght_bets[str(strength)] = int(line[1])
    
    strengths = sorted(strengths)
    for index, strength in enumerate(strengths):
        result += (index + 1) * dictionnary_strenght_bets[str(strength)]

    end_time_part1 = time.time()
    execution_duration_part1 = end_time_part1 - start_time_part1

    print("Part 1:", result)
    print(f"Part 1 took {execution_duration_part1} seconds to run.")

    # Part 2
    start_time_part2 = time.time()
    joker_value = 1

    result = 0
    strengths = []
    dictionnary_strenght_bets = {}

    
    with open(path) as file:
        data = file.readlines()
        for line in data:
            line = line.split()
            strength = give_global_hand_ranking_with_jokers(line[0], joker_value)
            strengths.append(strength)
            dictionnary_strenght_bets[str(strength)] = int(line[1])
    
    strengths = sorted(strengths)
    for index, strength in enumerate(strengths):
        result += (index + 1) * dictionnary_strenght_bets[str(strength)]

    end_time_part2 = time.time()
    execution_duration_part2 = end_time_part2 - start_time_part2

    print("Part 2:", result)
    print(f"Part 2 took {execution_duration_part2} seconds to run.")

if __name__ == "__main__":
    main()
