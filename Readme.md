Пример использования

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