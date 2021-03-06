def thesaurus(*args):
    result = {}
    for name in args:
        result.update({name[0]: list(filter(lambda el: el.startswith(f'{name[0]}'), args))})
    return result


def thesaurus_adv(*args):
    result_adv = {}
    for people in args:
        surname = str.split(people, ' ')[1][0]
        result_adv.update({surname: list(filter(lambda el: el[el.index(' ') + 1:].startswith(f'{surname}'), args))})
    for key in result_adv:
        result_adv[key] = thesaurus(*result_adv[key])
    return result_adv


final_dict = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(final_dict)

# отдельная сортировка словаря по ключам, без дополнительных библиотек
final_dict_sort = {}
for item in sorted(final_dict):
    final_dict_sort.update({item: final_dict[item]})
print(final_dict_sort)
