my_list = [57.8, 46.51, 97, 348, 11.23, 97, 38, 2, 43, 90.2, 30, 455, 36, 222, 451.54, 1, 123, 43.2, 13, 93]
print('ID of price list:', id(my_list))
my_list.sort()
print('ID of sorted price list:', id(my_list))
val_list = ''
for val in my_list:
    if my_list.index(val) < len(my_list) and isinstance(val, float):
        rub = str(val).split('.')[0]
        cope = str(val).split('.')[1]
        val_list += f'{rub} руб {cope:02} коп, '
    elif my_list.index(val) < len(my_list):
        val_list += f'{val} руб, '
print('Price list:', val_list.rstrip(', '))
print('---------------')
my_list.sort(reverse=True)
print('ID of reversed sorted price list:', id(my_list))
val_list_r = ''
for val in my_list[:5]:
    if my_list.index(val) < len(my_list[:5]) and isinstance(val, float):
        rub = str(val).split('.')[0]
        cope = str(val).split('.')[1]
        val_list_r += f'{rub} руб {cope:02} коп, '
    elif my_list[:5].index(val) < len(my_list[:5]):
        val_list_r += f'{val} руб, '
print('Top 5 price list:', val_list_r.rstrip(', '))
