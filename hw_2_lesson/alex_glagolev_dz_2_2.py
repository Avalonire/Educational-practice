my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']

# id(my_list) 1923282675328

idx = 0
while idx < (len(my_list)):
    if my_list[idx][-1:].isdigit() and not my_list[idx].count('.'):
        if -10 < int(my_list[idx]) < 0:
            my_list[idx] = '0'.join(my_list[idx])
        elif 0 < int(my_list[idx]) < 10:
            my_list[idx] = f'{0}{my_list[idx]}'
        my_list.insert((idx + 1), '"')
        my_list.insert(idx, '"')
        idx += 3
    idx += 1

# id(my_list) 1923282675328

result = ''
for item in my_list:
    if not item[-1:].isdigit():
        result += item + ' '
    elif item[-1:].isdigit():
        result = result[:-1] + item

print(result)
