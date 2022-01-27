items = ['яйца 2шт', 'сахар 1 л.', 'соль 1 чл.', 'уксус']
def format_ingredients(items):
    if len(items)==1:
        recept = items
    else:
        last = items.pop(-1)
        pre_last = items.pop(-1)
        without_last = items
        recept = ''
        for ingredient in without_last:
            recept += f'{ingredient}, '
        recept += f'{pre_last} '
        recept += f'и {last}'
    return recept

print(format_ingredients(items))



