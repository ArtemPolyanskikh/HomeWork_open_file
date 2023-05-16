from pprint import pprint

with open('text.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        num = int(file.readline())
        ingredient = []
        for i in range(num):
            ingredient_name, quantity, measure = file.readline().split(' | ')
            mid_list = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.strip()}
            ingredient.append(mid_list)
        file.readline()
        cook_book[dish] = ingredient


def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish in dishes:
        for i in cook_book[dish]:
            if i['ingredient_name'] in res:
                res['ingredient_name']['quantity'] = str(int(res['ingredient_name']['quantity']) + (int(i['quantity'] * person_count)))
            else:
                res[i['ingredient_name']] = {'measure': i['measure'], 'quantity': str(int(i['quantity']) * person_count)}
    pprint(res)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 4)