import re
import controller as cont

def parse_space(my_string: str):    # Убираем пробелы
    pars_str = my_string.replace(' ', '')
    return pars_str
def parse_num_list(my_string: str):     # Делаем список чисел
    number = re.findall(r'\d+', my_string)
    return number
def parse_operation_list(my_string: str):   # Делаем список операций
    operation_list = []
    for chair in my_string:
        if chair in ['+', '-', '*', '/']:
            operation_list.append(chair)
    return operation_list