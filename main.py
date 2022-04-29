import os


base_path = os.getcwd()
file_name = 'recipes'
full_path = os.path.join(base_path, file_name)

# Задание№1
cook_book = {}

def file_worker(file_name: str, mode: str, encoding: str):
    one_recipe = set()
    ingredients = []
    with open(file_name, mode, encoding=encoding) as file:
        for line in file:
            y = line.strip()
            one_recipe = dict.fromkeys([y])
            amount_ing = file.readline().strip()
            count = 0
            ingredients = []
            while count < int(amount_ing):
                count += 1
                ingred = file.readline().rstrip().split(' | ')
                d = {'ingredient_name': ingred[0], 'quantity': ingred[1], 'measure': ingred[2]}
                ingredients.append(d)
            one_recipe[y] = ingredients
            file.readline().strip()
            cook_book.update(one_recipe)
        print(f'Задание№1\ncook_book = {cook_book}\n')
        return (cook_book)

#Задание№2
#Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
#На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова
def get_shop_list_by_dishes(dishes: str, person_count: str):
    result_ing = {}
    result_rec = {}
    for k,v in cook_book.items():
        if k in dishes:
            for ing in v:
                for k,v in ing.items():
                    if k == 'ingredient_name':
                        x = ing.get(k)
                        ingg = ing.copy()
                        del ingg['ingredient_name']
                        result_rec[x] = ingg
                    if k == 'quantity':
                        ingg[k] = (int(ingg[k]) * person_count)
    print(f'Задание№2\n {result_rec}')

file_worker(file_name, 'r', 'utf-8')
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)




