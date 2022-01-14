my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
hello = input('Write your phrase: ')
for idx in range(len(my_list)):
    print(f'{hello}, {my_list[idx].split()[-1].title()}')
