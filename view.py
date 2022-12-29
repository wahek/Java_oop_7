cancel_chair = {'!', '@', '"', '#', '№', '$', ';', '%', '^', '&', '|', '?', '<', '>', ':', '~', '`'}


def choice():
    while True:
        try:
            print('Кнопочный калькулятор: 1 | Строчный калькулятор: 2')
            choice = int(input(':'))
            if choice in [1, 2]:
                return choice
        except:
            print('Ошибка')


def input_number():
    while True:
        try:
            number = int(input('Введите число: '))
            return number
        except:
            print('Ошибка')


def input_operation():
    while True:
        operation = input('Введите операцию: ')
        if operation in ['+', '-', '*', '=', '/']:
            return operation
        else:
            print('Введите корректную операцию')


def input_string_calculated():  # Ввод строки с проверками
    while True:
        try:
            string_calculated = input('Введите выражение для вычисления: ')
            string_calculated.lower().islower()  # Проверка наличия букв
            if set(string_calculated).intersection(cancel_chair) != set():  # Проверка вхождения запрещённых символов
                print('Некорректный ввод выражения')
            elif string_calculated.islower() == False:
                return string_calculated
            else:
                print('Некорректный ввод выражения')
        except:
            print('Ошибка')


def print_to_console(value_text):
    print(value_text)


def logg_off(result):
    print(f'Ответ = {result}| До свидания')


def print_division_zero():
    print('На 0 делить нельзя')
def print_string_calc(string, result):
    print(f'{string} = {result}')
