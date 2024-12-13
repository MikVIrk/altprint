# Пример использования


``` python

val1 = 'значение1'
val2 = 100500
val3 = np.arange(3,10,2)
list_ = [3, 5, 2]
clrs = {
    'black' : '30',
    'red' :  '31',
    'green' : '32',
    'yellow' : '33'}

mprint([['val1,val2, val3, type(val3), val3.shape'], [val1,val2, val3, type(val3), val3.shape]], 'Тест', len_box=50, symbol='*')
mprint([["type(list_), len(list_), list_", color='red'], [type(list_), len(list_), list_]], is_italic=False)
mprint([['type(clrs), clrs.keys(), clrs.values()'], [type(clrs), clrs.keys(), clrs.values()]], color='green', is_italic=True)

```
Пример использования в Google Colab:

``` python

!rm -rf altprint # Удаляем исходник
!git clone https://github.com/MikVIrk/altprint
import sys
sys.path.append("/content/altprint")
import altprint as alp
##############################################################################
# Функция для печати названий переменных и их значений из списка
###############################################################################
def mprint(str_of_variable,
           title='', len_box=40, symbol='-',
           color='blue', is_italic=False, is_bold=False):
    """
    Функция для печати названий переменных и их значений из списка

    colors:
        black, red, green, yellow, blue, violet, turquoise, white
    """

    str_var = [item.strip() for item in str_of_variable.split(',')]
    list_var  = [eval(i) for i in str_var]

    alp.mprint([str_var, list_var], title, len_box, symbol, color, is_italic, is_bold)
    pass


```
``` python
lst = ['foot', 'ball']
lst2 = ['Test', 'print', '666']

mprint('lst, lst2[2], len(lst), type(lst2), np.zeros(10000)', color='yellow', title='Тест печати', len_box=0)
mprint('lst, lst2[1], len(lst), type(lst2), np.zeros(10)', color='green', title='Тест печати зеленым', symbol='*')
```
Вывод:

![alt text](images/image.png)

## Ещё пример

``` python
val1 = 'значение1'
val2 = 100500
val3 = np.arange(3,10,2)
list_ = [3, 5, 2]
clrs = {
    'black' : '30',
    'red' :  '31',
    'green' : '32',
    'yellow' : '33'}

mprint('val1,val2, val3, type(val3), val3.shape')
mprint("type(list_), len(list_), list_")
mprint('type(clrs), clrs.keys(), clrs.values()', color='red', is_italic=True)
```
Вывод:

![alt text](images/image-1.png)

Смысл функции в том, что мы передаём в неё список переменных разделённых запятой в виде строки, а на выходе получаем вывод в виде: 
  
><span style="color:violet">Переменная1:</span>  ЗначениеПеременной1 

><span style="color:violet">Переменная2:</span>  ЗначениеПеременной2
  
>и т.д.

Это очень удобно при отладке кода.