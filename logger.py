def logger(text: str):  # Запись текста в history
    with open('history.txt', 'a') as data:
        data.write(text)


def log_new_str():  # Переход на новую строку
    with open('history.txt', 'a') as data:
        data.write('\n')

def logger_str(text, text_2: str):  # Вывод строки и ответа в строчном калькуляторе
    with open('history.txt', 'a') as data:
        data.write(f'{text} = {text_2}')