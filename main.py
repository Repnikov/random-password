import random
import sys

number_entry = True

while number_entry:
    pass_count = input('Введи количество символов для генерации пароля:\n')
    try:
        if pass_count == '' or int(pass_count) == 0:
            # по умолчанию пароль из 9 символов
            print('количество по умолчанию 9 символов')
            pass_count = 9
            number_entry = False
        else:
            pass_count = int(pass_count)
            number_entry = False
    except ValueError:
        print('Необходимо ввести количество символов для создания пароля')

# alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
symbols = '~!@#$%^&*()_+=-?><:"|;[]{}./№'


# Функция для генерации паролей
def randon_gen(alphabet: str, symbol: str, number: str, count: int):
    counter = 0
    total = ''
    while counter < count:
        alphabet_symbol = random.choice(alphabet)
        alphabet_symbol_big = random.choice(alphabet.upper())
        symbols_symbol = random.choice(symbol)
        numbers_symbol = random.choice(number)
        new_pass = random.choice(alphabet_symbol + symbols_symbol + numbers_symbol + alphabet_symbol_big)

        total += new_pass
        counter += 1

    return total[0:count]


generated_password = randon_gen(alphabet_en, numbers, symbols, pass_count)
print(f'Твой сгенерированный пароль: {generated_password}')

print(sys.stdin.readline())
