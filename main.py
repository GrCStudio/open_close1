def file_import():
    result = dict()
    with open("recipes.txt", 'r', encoding='utf-8') as file:
        for line in file:
            dish = line.strip()
            ingridients_quantity = int(file.readline().strip())
            ingridients_list = []
            for ingridient in range(ingridients_quantity):
                strline = file.readline().strip()
                lineoutput = ''
                counter = 1
                for character in strline:
                    if character != '|':
                        lineoutput += character
                    else:
                        if counter == 1:
                            ingredient_name = lineoutput.strip()
                        elif counter == 2:
                            quantity = int(lineoutput.strip())
                        lineoutput = ''
                        counter += 1
                measure = lineoutput.strip()
                ingridients_list.append({'ingredient_name': ingredient_name,
                                         'quantity': quantity,
                                         'measure': measure})
            result[dish] = ingridients_list
            file.readline()
        return result


def get_shop_list_by_dishes(dishes, person_count):
    result = dict()
    for dish in dishes:
        for inrgidients in cook_book[dish]:
            ingredient_name = inrgidients["ingredient_name"]
            quantity = inrgidients["quantity"] * person_count
            measure = inrgidients["measure"]
            if result.get(ingredient_name) is None:
                result[ingredient_name] = {"quantity": quantity, "measure": measure}
            else:
                result[ingredient_name]['quantity'] += quantity
    return result


cook_book = file_import()
#print(cook_book)
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
