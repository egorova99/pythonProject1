import os

base_path = os.getcwd()
file_name = 'recipes'
full_path = os.path.join(base_path, file_name)

# Задание№1

class Kitchen:
 def __init__(self):
  self.cook_book = {}
 def file_worker(self, file_name: str, mode: str, encoding: str):
  one_recipe = set()
  ingredients = []
  with open(file_name, mode, encoding=encoding) as file:
    #cook_book = {}
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
        #print(one_recipe)
        file.readline().strip()
        self.cook_book.update(one_recipe)
    print(f'Задание№1\ncook_book = {self.cook_book}\n')
    return (self.cook_book)


#Задание№2
#Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
#На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова

 def get_shop_list_by_dishes(self, dishes, person_count):
    result_ing = {}
    result_rec = {}
    for k,v in self.cook_book.items():
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


result = Kitchen()
result.file_worker(file_name, 'r', 'utf-8')
result.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)






#{
#  'Картофель': {'measure': 'кг', 'quantity': 2},
#  'Молоко': {'measure': 'мл', 'quantity': 200},
 # 'Помидор': {'measure': 'шт', 'quantity': 4},
 # 'Сыр гауда': {'measure': 'г', 'quantity': 200},
#  'Яйцо': {'measure': 'шт', 'quantity': 4},
#  'Чеснок': {'measure': 'зубч', 'quantity': 6}
#}
