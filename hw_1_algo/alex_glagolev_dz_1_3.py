percents = list(range(1, 100 + 1))
for idx in range(len(percents)):
    if percents[idx] % 10 == 1 and percents[idx] != 11:
        print(percents[idx], 'процент')
    elif 1 < percents[idx] % 10 <= 4 and not 11 < percents[idx] < 15:
        print(percents[idx], 'процента')
    elif percents[idx] % 10 > 4 or percents[idx] % 10 == 0 or 10 < percents[idx] < 15:
        print(percents[idx], 'процентов')
