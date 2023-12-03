# Partie 1
def sum_calibration_values_part1(lines):
    total_sum = 0

    for line in lines:
        # Trouver tous les entiers dans la ligne
        digits = [int(digit) for digit in line if digit.isdigit()]

        # Utiliser le premier et le dernier entier pour former la valeur de calibration
        first_digit = digits[0]
        last_digit = digits[-1]

        # Ajouter la somme à la valeur totale
        total_sum += (first_digit * 10 + last_digit)

    return total_sum


# Exemple d'utilisation
lines_part1 = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
result_part1 = sum_calibration_values_part1(lines_part1)
print(result_part1)

# Partie 2
def sum_calibration_values_part2(lines):
    total_sum = 0

    # Dictionnaire pour mapper les mots aux chiffres
    word_to_digit = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for line in lines:
        # Remplacer les mots par les chiffres correspondants
        for word, digit in word_to_digit.items():
            line = line.replace(word, digit)

        # Construire les chiffres à partir des caractères consécutifs
        digits = []
        current_digit = ''

        for char in line:
            if char.isdigit():
                current_digit += char
            elif current_digit:
                digits.append(int(current_digit))
                current_digit = ''

        if current_digit:
            digits.append(int(current_digit))

        # Utiliser la somme des chiffres pour former la valeur de calibration
        total_sum += sum(digits)

    return total_sum


# Exemple d'utilisation
lines_part2 = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
result_part2 = sum_calibration_values_part2(lines_part2)
print(result_part2)



# Exemple d'utilisation
# lines_part2 = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
lines_part2 = ["eightwothree"]
result_part2 = sum_calibration_values_part2(lines_part2)
print(result_part2)
