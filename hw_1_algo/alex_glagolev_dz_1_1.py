duration = int(input('duration = '))
while duration >= 0:
    sec = duration % 60
    min = duration // 60 % 60
    hour = duration // 60 ** 2 % 24
    day = duration // (60 ** 2 * 24)
    if duration < 60:
        print(sec, 'сек')
    elif 3600 > duration >= 60:
        print(min, 'мин', sec, 'сек')
    elif 86400 > duration >= 3600:
        print(hour, 'час', min, 'мин', sec, 'сек')
    elif duration >= 86400:
        print(day, 'дн', hour, 'час', min, 'мин', sec, 'сек')
    duration = int(input('duration = '))
print('Invalid value! You need to enter a value in seconds! Program stop.')
