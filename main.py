''' Задача №2.
Нужно написать функцию, которая на вход принимает список блюд из cook_book
и количество персон для кого мы будем готовить. На выходе мы должны получить словарь с
названием ингредиентов и его количества для блюда'''

cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}

from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count):
    dict_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            print(dish)
            for ingredient in cook_book[dish]:
                dict_dishes[ingredient['ingredient_name']] = {'quantity': ingredient['quantity'] * person_count, 'measure': ingredient['measure']}
    return dict_dishes

res = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(res, width=100, sort_dicts=False)