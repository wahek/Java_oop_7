first_number = 0
second_number = 0
operation = ''
result = 0
string_calc = ''
number_list = []
operation_list = []


def get_number_list():
    global number_list
    return number_list


def get_operation_list():
    global operation_list
    return operation_list


def get_string_calc():
    global string_calc
    return string_calc


def get_first():
    global first_number
    return first_number


def get_second():
    global second_number
    return second_number


def get_operation():
    global operation
    return operation


def get_result():
    global result
    return result


def set_number_list(value):
    global number_list
    number_list = value


def set_operation_list(value):
    global operation_list
    operation_list = value


def set_string_calc(strin):
    global string_calc
    string_calc = strin


def set_first(value):
    global first_number
    first_number = value


def set_second(value):
    global second_number
    second_number = value


def set_operation(value):
    global operation
    operation = value


def addition():
    global first_number
    global second_number
    global result
    result = first_number + second_number


def difference():
    global first_number
    global second_number
    global result
    result = first_number - second_number


def multiplication():
    global first_number
    global second_number
    global result
    result = first_number * second_number


def devision():
    global first_number
    global second_number
    global result
    result = first_number / second_number
    if result == int(result):
        result = int(result)

def solution_string():
    global number_list
    global operation_list
    global result
    while number_list != []:
        for i in range(len(operation_list)):
            if operation_list[i] == '*':
                temp = int(number_list[i]) * int(number_list[i + 1])
                number_list[i] = temp
                number_list.pop(i + 1)
            elif operation_list[i] == '/':
                temp = int(number_list[i]) / int(number_list[i + 1])
                number_list[i] = temp
                number_list.pop(i+1)
        result = number_list


