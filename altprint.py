import numpy as np
##############################################################################
# Функция для печати названий переменных и их значений из списка
###############################################################################
def mprint(str_var,
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


    list_var = [item.strip() for item in str_var.split(',')]
    if title == '':
        print(symbol * len_box)
    else:
        start_str = symbol*0
        end_str = symbol*(len_box-1-len(title))
        print(f'{start_str}\033[{colors.get(color)}m{title} \033[0m{end_str}')
    # print()

    for var in list_var:
        # print(var)
        print(f'  {color_start}{var}:{color_end} {eval(var)}')

    print(symbol * len_box)


# Пример использования
val1 = 'значение1'
val2 = 100500
val3 = np.arange(3,10,2)
list_ = [3, 5, 2]
clrs = {
    'black' : '30',
    'red' :  '31',
    'green' : '32',
    'yellow' : '33'}

mprint('val1,val2, val3, type(val3), val3.shape', 'Тест', len_box=50, symbol='*')
mprint("type(list_), len(list_), list_", color='red', is_italic=False)
mprint('type(clrs), clrs.keys(), clrs.values()', color='green', is_italic=True)