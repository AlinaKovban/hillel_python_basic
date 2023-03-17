from random import randint

first_list =[randint(1,10) for i in range(1,201)]

dic_list = {item: first_list.count(item) for item in first_list}

dic_sorted = dict(sorted(dict.items(dic_list)))


def total():
        for key in dic_sorted:
                print(f'Число {key} встречается в первоначальном списке {dic_sorted[key]}')


total()
