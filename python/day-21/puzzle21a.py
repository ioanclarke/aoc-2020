fin = open('input.txt')
data = fin.read().split('\n')
del data[-1]
ing_list = []
al_list = []
for line in data:
    ingredients = line[:line.find('(') - 1]
    allergens = line[line.find('(') +  10 : -1]
    ing_list.append(ingredients.split(' '))
    al_list.append(list(map(str.strip, allergens.split(','))))

al_to_ing_map = {}
for allergens, ingredients in zip(al_list, ing_list):
    for al in allergens:
        #print(f'{al} must be in one of {set(ingredients)}')
        al_to_ing_map[al] = al_to_ing_map.get(al, set(ingredients)).intersection(set(ingredients))

allergenic_ings = set()
for val in al_to_ing_map.values():
    for ing in val:
        allergenic_ings.add(ing)

count = 0
for ings in ing_list:
    for ing in ings:
        if ing not in allergenic_ings:
            count += 1
print(count)
