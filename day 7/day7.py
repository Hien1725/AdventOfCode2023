import time

def hand_ranking(s, joker_rule_active):
    '''Evaluate the ranking of a poker hand represented by a string of 5 characters.

    Args:
        s (str): A string containing 5 characters, representing cards.
                Each character can be one of the following: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
        joker_rule_active (bool): A boolean indicating whether the "Joker Rule" is active.
                                  If True, J cards are considered wildcards and can act as any card to form the strongest hand.

    Returns:
        int: The ranking of the poker hand, considering the optional Joker Rule.
             Possible values:
             6 - Five of a kind - 1 occurrence of 5 - 1
             5 - Four of a kind - 1 occurrence of 4 - 1 and 1 occurrence of 1 - 2
             4 - Full house - 1 occurrence of 3 and 1 occurrence of 2 - 2
             3 - Three of a kind - 1 occurrence of 3 and 1 occurrence of 1 and 1 occurrence of 1 - 3
             2 - Two pairs - 2 occurrences of 2 and 1 occurrence of 1 - 3
             1 - One pair - 1 occurrence of 2 and 3 occurrences of 1 - 4
             0 - High card - 5 occurrences of 1 - 5

    Note:
        If the Joker Rule is active (joker_rule_active=True), J cards are treated as wildcards, potentially enhancing the hand's strength.
        The J cards can act as any card necessary to form the strongest hand. However, for tie-breaking purposes, J is always considered weaker than other non-wildcard cards.
    '''

    occurrences = {}
    for char in s:
        # Increment the count of the current character in the dictionary
        occurrences[char] = occurrences.get(char, 0) + 1
    
    # Check if the joker rule is active
    if joker_rule_active:
        number_of_J = s.count('J')

        if 'J' in occurrences:
            del occurrences['J']

            # Check if occurrences is now empty, and return 6 if true (s was 'JJJJJ')
            if occurrences == {}:
                return 6
        
        # Increase the count of the most frequent character by the number_of_J (considering joker rule)
        occurrences[max(occurrences, key=occurrences.get)] += number_of_J

    diff_cards = len(occurrences)
    if diff_cards == 1:
        return 6
    elif diff_cards == 2 and max(occurrences.values()) == 4:
        return 5
    elif diff_cards == 2:
        return 4
    elif diff_cards == 3 and max(occurrences.values()) == 3:
        return 3
    elif diff_cards == 3:
        return 2
    elif diff_cards == 4:
        return 1
    else:
        return 0

def give_card_ranking(char, joker_value):
    '''Assign a numerical value to a playing card character.
    
    Args:
        char (str): A character representing a playing card (A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2).
        joker_value (int): The value assigned to the Joker card, influencing its ranking.

    Returns:
        int: The numerical value assigned to the playing card character, considering the joker_value.
    '''

    cards_values = {'A' : 14, 'K' : 13, 'Q' : 12, 'J' : joker_value, 'T' : 10, '9' : 9, '8' : 8, '7' : 7, '6' : 6, '5' : 5, '4' : 4, '3' : 3, '2' : 2}
    return cards_values.get(char)

def give_hand_ranking(s, joker_value):
    '''Assign a numeric value to the strength of a poker hand based on individual card values.
    
    Args:
        s (str): A string containing 5 characters, representing poker cards in a hand.
                Each character can be one of the following: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
        joker_value (int): The value assigned to the Joker card, influencing its ranking.

    Returns:
        int: The numeric value representing the strength of the poker hand.
    '''

    rst = 0
    
    for i in range(0, len(s)):
        dec_i = len(s) - (i + 1)
        rst += give_card_ranking(s[i], joker_value) * (10 ** (2 * dec_i))

    return rst

def give_global_hand_ranking(s, joker_value, joker_rule_active):
    '''Assign the total strength value to a poker hand, considering both the individual card values and potential Jokers.
    
    Args:
        s (str): A string containing 5 characters, representing poker cards in a hand.
                Each character can be one of the following: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
        joker_value (int): The value assigned to the Joker card, influencing its ranking.
        joker_rule_active (bool): A boolean indicating whether the "Joker rules" are in effect.

    Returns:
        int: The total strength value of the poker hand, accounting for both card values and Jokers.
    '''

    return hand_ranking(s, joker_rule_active) * 10**10 + give_hand_ranking(s, joker_value)

def main():
    """
    Solve the Day 7 challenge of Advent of Code 2023.

    This function reads data from an input file, calculates poker hand rankings based on the rules specified,
    and then calculates the total winnings for two scenarios: one without Joker rules (Part 1) and one with Joker rules (Part 2).

    Returns:
        None
    """
    
    # Define the path to the input file
    path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 7\\input.txt"
    # path = "C:\\Users\\duche\\Desktop\\Advent of Code 2023\\day 7\\input_test.txt"

    # Part 1
    start_time_part1 = time.time()
    joker_value = 11

    result = 0
    strengths = []
    dictionnary_strenght_bets = {}

    # Read data from the file and calculate hand rankings without Joker rules
    with open(path) as file:
        data = file.readlines()
        for line in data:
            line = line.split()
            strength = give_global_hand_ranking(line[0], joker_value, False)
            strengths.append(strength)
            dictionnary_strenght_bets[str(strength)] = int(line[1])

    # Sort hand strengths and calculate the result
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

    # Read data from the file and calculate hand rankings with Joker rules
    with open(path) as file:
        data = file.readlines()
        for line in data:
            line = line.split()
            strength = give_global_hand_ranking(line[0], joker_value, True)
            strengths.append(strength)
            dictionnary_strenght_bets[str(strength)] = int(line[1])
    
    # Sort hand strengths and calculate the result for Part 2
    strengths = sorted(strengths)
    for index, strength in enumerate(strengths):
        result += (index + 1) * dictionnary_strenght_bets[str(strength)]

    end_time_part2 = time.time()
    execution_duration_part2 = end_time_part2 - start_time_part2

    print("Part 2:", result)
    print(f"Part 2 took {execution_duration_part2} seconds to run.")

if __name__ == "__main__":
    main()
