import numpy as np
##############################################################################
# Функция для печати названий переменных и их значений из списка
###############################################################################
def mprint(variables,
           title='', len_box=40, symbol='-',
           color='blue',
           is_italic=False,
           is_bold=False):

    '''
    Args:
        str_var - строка в виде 'val1, val2, type(val3), val3.shape' и т.д.
        len_box - Длина срочки из символов (symbol)
        symbol

        выводит на печать переменные и их значения в виде:
            val1: значение1
            val2: значение2

          Таблица с цветами  https://habr.com/ru/sandbox/158854/
          https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
    '''
    # Словарь с кодами цветов
    colors = {
        'black' : '30',
        'red' :  '31',
        'green' : '32',
        'yellow' : '33',
        'blue' : '34',
        'violet' : '35',
        'turquoise' : '36',
        'white' : '37'
    }

    if is_italic:
        italic = '\033[3m'
    else:
        italic = ''
    if is_bold:
        bold = '\033[1m'
    else:
        bold = ''

    color_start = f'\033[{colors.get(color)}m{italic}{bold}'
    color_end = '\033[0m'

    # variables
    str_var = variables[0]
    list_var = variables[1]

    if title == '':
        print(symbol * len_box)
    else:
        start_str = symbol*0
        end_str = symbol*(len_box-1-len(title))
        print(f'{start_str}\033[{colors.get(color)}m{title} \033[0m{end_str}')
    # print()

    for i in range(len(list_var)):
        # print(var)
        print(f'  {color_start}{str_var[i]}:{color_end} {list_var[i]}')

    print(symbol * len_box)