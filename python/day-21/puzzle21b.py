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



answered = {}
for i in range(len(al_to_ing_map)):
    for k,v in al_to_ing_map.items():
        if not k in answered and len(v) == 1:
            val, = v
            definite = (k, val)
            answered[k] = None
            break

    for k,v in al_to_ing_map.items():
        if k != definite[0] and definite[1] in v:
            al_to_ing_map[k].remove(definite[1])

# for k,v in al_to_ing_map.items():
#     print(k,v)

sorted_allergens = sorted(al_to_ing_map)
print(sorted_allergens)
output_ings = []
for al in sorted_allergens:
    val, = al_to_ing_map[al]
    output_ings.append(val)

print(','.join(output_ings))
# allergenic_ings = set()
# for val in al_to_ing_map.values():
#     for ing in val:
#         allergenic_ings.add(ing)
