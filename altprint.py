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
        print(f'  {color_start}{str_var[i]}:{color_end} {list_var[i]}')

    print(symbol * len_box)

##############################################################################
# Функция, упрощающая вывод текста в цвете
###############################################################################
def cprint(*args, sep=' ', end='\n', is_visible=True):
    """
    Prints text in different colors

    Args:
        *args:  Unlimited number of arguments to print.
        sep: Separator between arguments (default: ' ').
        end: Character to print at the end (default: '\n').

        colors: |r - red
                |g - green
                |y - yellow
                |b - blue
                |v - violet
                |t - turquoise
                |w - whait
                || - сanceling color printing
        other:  |B - bold
                |I - italic
    """
    # sep, end = ' ', '\n'
    dict_color = {'||': '\033[0m', '|r': '\033[31m', '|g': '\033[32m', '|y': '\033[33m',
                  '|b': '\033[34m', '|v': '\033[35m', '|t': '\033[36m', '|w': '\033[37m',
                  '|B': '\033[1m', '|I': '\033[3m'}

    args = list(args)
    args_new = args.copy()
    str_for_print = ''

    # Если разделитель не знак пробела и цвет задан отдельным аргументом,
    #   то для того, чтобы не печатать лишние разделители,
    #   аргумент цвета присоединяется к соседнему аргументу.

    # Обработка начали списка аргументов
    for i in range(len(args)):
        ind = i

        separate = '' if i == len(args) - 1 else sep

        if str(args[ind]).strip() in dict_color.keys():

            args_new[1] = args_new[0] + str(args_new[1])
            args_new.pop(0)

        else:
            break

    # Обработка конца списка аргументов
    args = args_new.copy()

    for i in range(len(args), 0, -1):
        ind = i-1

        if str(args[ind]).strip() in dict_color.keys():
            args_new[ind-1] = str(args_new[ind-1]) + args_new[ind]
            args_new.pop(ind)
        else:
            break

    # Обработка середины списка аргументов
    for i in range(len(args_new)):
        separate = '' if str(args_new[i]).strip() in dict_color.keys() or i==len(args_new)-1 else sep
        str_for_print = str_for_print + str(args_new[i]) + separate

    # Замена на паттерны форматирования
    for j in dict_color.keys():

        str_for_print = str_for_print.replace(str(j), dict_color[j])
    
    if is_visible:
        print(str_for_print, end=end)
    
    return str_for_print + end