import logger
import view
import model
import parser

def input_first():
    number = view.input_number()
    model.set_first(number)


def input_second():
    while True:
        number = view.input_number()
        if model.get_operation() == '/' and number == 0:
            view.print_division_zero()
        else:
            model.set_second(number)
            break


def input_operation():
    operat = view.input_operation()
    model.set_operation(operat)


def input_string_cacl():
    string_calculate = view.input_string_calculated()
    model.set_string_calc(string_calculate)


def solution():
    oper = model.get_operation()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper == '/':
        model.devision()
    elif oper == '*':
        model.multiplication()
    else:
        return True
    result_string = f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'
    view.print_to_console(result_string)
    model.set_first(model.get_result())
    return False


def start():
    choice = view.choice()
    if choice == 1:
        input_first()
        logger.logger(str(model.get_first()))
        while True:
            input_operation()
            logger.logger(model.get_operation())
            if model.get_operation() == '=':
                view.logg_off(model.get_result())
                logger.logger(str(model.get_result()))
                logger.log_new_str()
                break
            input_second()
            logger.logger(str(model.get_second()))
            solution()
            logger.logger('=')
            logger.logger(str(model.get_result()))
            logger.log_new_str()
            logger.logger(str(model.get_result()))
    elif choice == 2:
        input_string_cacl()
        model.set_string_calc(parser.parse_space(model.get_string_calc()))
        model.set_operation_list(parser.parse_operation_list(model.get_string_calc()))
        model.set_number_list(parser.parse_num_list(model.get_string_calc()))
        model.solution_string()
        view.print_string_calc(model.get_string_calc(), model.get_result())
        logger.logger_str(model.get_string_calc(), model.get_result())
        logger.log_new_str()