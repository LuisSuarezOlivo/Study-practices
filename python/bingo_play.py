
def bingo_game(numbers):
    bingo_word = [2, 9, 14, 7, 15]
    bingo_letters = "BINGO"

    number_counts = {}
    for number in numbers:
        if 1 <= number <= 26:
            if number in number_counts:
                number_counts[number] += 1
            else:
                number_counts[number] = 1

    for letter, num in zip(bingo_letters, bingo_word):
        if num not in number_counts or number_counts[num] == 0:
            return "LOSE"
    else:
        number_counts[num] -= 1

    return "WIN"


# Ejemplo 1 (WIN)
ejemplo_win = [2, 14, 7, 22, 9, 15, 11, 5, 8, 19]
resultado_win = bingo_game(ejemplo_win)
print("frist", resultado_win)

# Ejemplo 2 (LOSE - falta el número 2)
ejemplo_lose = [14, 7, 22, 9, 15, 11, 5, 8, 19]
resultado_lose = bingo_game(ejemplo_lose)
print("second", resultado_lose)